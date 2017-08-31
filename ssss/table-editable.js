var TableEditable = function () {
//这里用的是jQueryr datables插件
    return {

        //main function to initiate the module
        init: function () {
            function restoreRow(oTable, nRow) {
                var aData = oTable.fnGetData(nRow);
                //alert("aData"+aData)
                var jqTds = $('>td', nRow);
                for (var i = 0, iLen = jqTds.length; i < iLen; i++) {
                    oTable.fnUpdate(aData[i], nRow, i, false);
                }

                oTable.fnDraw();
            }
			
			
            function editRow(oTable, nRow) {
                var aData = oTable.fnGetData(nRow);
                var jqTds = $('>td', nRow);
                //aData[0].substring(aData[0].indexOf(">")+1,aData[0].indexOf("</"))
                jqTds[0].innerHTML = '<input type="text" class="input-mini" value="' + aData[0] + '">';
                jqTds[1].innerHTML = '<input type="text" class="input-mini" value="' + aData[1] + '">';
                jqTds[2].innerHTML = '<input type="text" class="input-mini" value="' + aData[2] + '">';
                jqTds[3].innerHTML = '<input type="text" class="input-mini" value="' + aData[3] + '">';
                jqTds[4].innerHTML = '<input type="text" class="input-mini" value="' + aData[4] + '">';
                jqTds[5].innerHTML = '<input type="text" class="input-mini" value="' + aData[5] + '">';
                jqTds[6].innerHTML = '<input type="text" class="input-mini" value="' + aData[6] + '">';
                jqTds[7].innerHTML = '<a class="edit" href="">Save</a>';
                jqTds[8].innerHTML = '<a class="cancel" href="">Cancel</a>';
            }

            function saveRow(oTable, nRow) {
                var jqInputs = $('input', nRow);//获取行的input对象
                var aData = oTable.fnGetData(nRow);//获取表中行的对象
                //这是该行的所有内容
                oTable.fnUpdate(jqInputs[0].value, nRow, 0, true);
                oTable.fnUpdate(jqInputs[1].value, nRow, 1, true);
                oTable.fnUpdate(jqInputs[2].value, nRow, 2, true);
                oTable.fnUpdate(jqInputs[3].value, nRow, 3, true);
                oTable.fnUpdate(jqInputs[4].value, nRow, 4, true);
                oTable.fnUpdate(jqInputs[5].value, nRow, 5, true);
                oTable.fnUpdate(jqInputs[6].value, nRow, 6, true);
                oTable.fnUpdate('<a class="edit" href="">Edit</a>', nRow, 7, true);
                oTable.fnUpdate('<a class="delete" href="">Delete</a>', nRow, 8, true);
                oTable.fnDraw();
                //获取表中edit时每行的列值
                var jsonStr = ""
                for(var i=0;i<=jqInputs.length-1;i++){
                	//#跑到最后一个时做特殊处理，这里不
                	if (i==jqInputs.length-1){
                		jsonStr += aData[i]+"}"; 
                		break;
                		}
                	jsonStr += aData[i]+","; 
                	}
                	
			    $.get("/table_editable/",{'jsonStr':jsonStr}, function(ret){
			    //接收来自后台返回的数据
			    	 //将表的第一行数据alex修改为ret.result123
			    	 oTable.fnUpdate(ret.result, nRow, 0, false);
			    	 //<a href="/mod_dev/?ip={{ ip.ip }}" class="btn mini green-stripe">{{ ip.ip }}</a>
			        })
            }

            function cancelEditRow(oTable, nRow) {
                var jqInputs = $('input', nRow);
                oTable.fnUpdate(jqInputs[0].value, nRow, 0, false);
                oTable.fnUpdate(jqInputs[1].value, nRow, 1, false);
                oTable.fnUpdate(jqInputs[2].value, nRow, 2, false);
                oTable.fnUpdate(jqInputs[3].value, nRow, 3, false);
                oTable.fnUpdate(jqInputs[4].value, nRow, 4, false);
                oTable.fnUpdate(jqInputs[5].value, nRow, 5, false);
                oTable.fnUpdate(jqInputs[6].value, nRow, 6, false);
                oTable.fnUpdate('<a class="edit" href="">Edit</a>', nRow, 7, true);
                oTable.fnDraw();
            }

            var oTable = $('#sample_editable_1').dataTable({
                "aLengthMenu": [
                    [5, 15, 20, -1],
                    [5, 15, 20, "All"] // change per page values here
                ],
                // set the initial value
                "iDisplayLength": 5,
                "sDom": "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
                "sPaginationType": "bootstrap",
                "oLanguage": {
                    "sLengthMenu": "_MENU_ records per page",
                    "oPaginate": {
                        "sPrevious": "Prev",
                        "sNext": "Next"
                    }
                },
                "aoColumnDefs": [{
                //自定义表的排序规则
                        'bSortable': true,
                        'aTargets': [0]
                    }
                ]
            });

            jQuery('#sample_editable_1_wrapper .dataTables_filter input').addClass("m-wrap medium"); // modify table search input
            jQuery('#sample_editable_1_wrapper .dataTables_length select').addClass("m-wrap small"); // modify table per page dropdown
            jQuery('#sample_editable_1_wrapper .dataTables_length select').select2({
                showSearchInput : false //hide search box with special css class
            }); // initialzie select2 dropdown

            var nEditing = null;

            $('#sample_editable_1_new').click(function (e) {
                e.preventDefault();
                var aiNew = oTable.fnAddData(['', '', '', '','','','',
                        '<a class="edit" href="">Edit</a>', '<a class="cancel" data-mode="new" href="">Cancel</a>'
                ]);
                var nRow = oTable.fnGetNodes(aiNew[0]);
                editRow(oTable, nRow);
                nEditing = nRow;
            });

            $('#sample_editable_1 a.delete').live('click', function (e) {
                e.preventDefault();

                if (confirm("Are you sure to delete this row ?") == false) {
                    return;
                }
                var nRow = $(this).parents('tr')[0];
                
					
                //alert("Deleted! Do not forget to do some ajax to sync with backend :)");
                //准备删除表的数据
                var aData = oTable.fnGetData(nRow);
                //get IP
                //alert("aData"+aData[0])
                var Delete_jsonStr = aData[0]
                oTable.fnDeleteRow(nRow);
                $.get("/table_editable/",{'Delete_jsonStr':Delete_jsonStr}, function(ret){
			    //接收来自后台返回的数据
			    	 //将表的第一行数据alex修改为ret.result123
			    	 oTable.fnUpdate(ret.result, nRow, 0, false);
			        })
			     //delete要放在最后面，否则的话行的索引值会变
			    
            });

            $('#sample_editable_1 a.cancel').live('click', function (e) {
                e.preventDefault();
                if ($(this).attr("data-mode") == "new") {
                    var nRow = $(this).parents('tr')[0];
                    oTable.fnDeleteRow(nRow);
                } else {
                    restoreRow(oTable, nEditing);
                    nEditing = null;
                }
            });

            $('#sample_editable_1 a.edit').live('click', function (e) {
                e.preventDefault();
				
                /* Get the row as a parent of the link that was clicked on */
                var nRow = $(this).parents('tr')[0];

                if (nEditing !== null && nEditing != nRow) {
                    /* Currently editing - but not this row - restore the old before continuing to edit mode */
                    restoreRow(oTable, nEditing);
                    editRow(oTable, nRow);
                    nEditing = nRow;
                } else if (nEditing == nRow && this.innerHTML == "Save") {
                    /* Editing this row and want to save it */
                    saveRow(oTable, nEditing);
                    nEditing = null;
                    var s = jQuery(this).closest("tr").find("td").eq(1).text()
                   // alert("Updated! Do not forget to do some ajax to sync with backend :)");
                    
                } else {
                    /* No edit in progress - let's start one */
                    editRow(oTable, nRow);
                    nEditing = nRow;
                }
            });
        }

    };

}();