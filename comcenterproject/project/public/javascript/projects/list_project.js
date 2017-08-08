Ext.namespace("projects");

function currentSumBudget (value, cell, record){
 
	var total = Ext.util.Format.currency(value , '฿', 2,true);
	 return     '<span style="color:green;">' + total + '</span>'; 
}
function currentBudget(value, cell, record){
	var total = Ext.util.Format.currency(value , '฿', 2,true);
	return     '<span style="color:green;">' + total + '</span>'; 
}

function currentDetail (value, cell, record){
	return '<textarea readonly class="x-form-textarea x-form-field">' + value +'</textarea>';
}
function currentStatus (value, cell, record){
	var status = 1;
	if(record.data.project_status_id != null){
		 status = parseInt(record.data.project_status_id,10);
	}
 
	var colorStatus = "color:#FFCC00;";
	
	if(status == 2){
		colorStatus = "color:green;";
	}else{
		if(status == 3){
			colorStatus = "color:red;";
		}else
		{
			if(status == 4){
				colorStatus = "color:blue;";
			}else
			{
				if(status == 5){
					colorStatus = "color:#556B2F;";
				} 
			}
		}
	}
	
	return     '<span style="'+colorStatus + '">' + value + '</span>'; 
}

projects.gridProject = Ext.extend(Ext.grid.Panel,{
	store: Ext.data.StoreManager.lookup('listProjectStore'),
	columns: [
	//	{header: 'ปีงบประมาณ', width:70,  dataIndex: 'fiscal_year'},
		{header: 'ประเภท',  dataIndex: 'project_type'},
        {header: 'โครงการ',  dataIndex: 'project_name'},
        {header: 'งบประมาณรวม',align: 'right', dataIndex: 'allBudget',renderer : currentSumBudget },
		{header: 'เงินงบประมาณ',align: 'right', dataIndex: 'project_budget',renderer : currentBudget },
		{header: 'เงินบำรุง',align: 'right', dataIndex: 'maintenance_funds_budget',renderer : currentBudget },
		{header: 'งบประมาณอื่น',align: 'right', dataIndex: 'budget_other',renderer : currentBudget },
        {header: 'ผู้รับผิดชอบ', dataIndex: 'user_name'},
        {header: 'สถานะ', width:110,dataIndex: 'project_status',renderer :currentStatus} 
        
    //  ,  {header: 'แผนก/ฝ่าย', dataIndex: 'division'},
    //    {header: 'หน่วย/งาน', dataIndex: 'section'},
    //    {header: 'รายละเอียด',width:200, dataIndex: 'detail',renderer :currentDetail}
        
    ] 
	
	
});

projects.ListProject = Ext.extend(Ext.form.Panel,{
	//title:'แสดงรายการโครงการ',
	autoWidth : true,
	//autoHeight: true,
	height : 600 ,
	loadDataSearch : function(){
		fiscalyear = this.fiscalyear.getValue();
    	division = this.division.getValue();
    	section = this.section.getValue();
    	searchstatus = this.searchstatus.getValue();
  		projectType = this.projectType.getValue();
    	 
    	projects.listProjectStore.load({
    		params:{
				 
				start : 0,
				limit :  25,
		 		fiscalyear: fiscalyear,
		 		division : division,
		 		section: section,
		 		status: searchstatus ,
		 		projectType : projectType
       		}
    	});
	},
	exportToExcel : function(){
		var main = this;
		fiscalyear = this.fiscalyear.getValue();
    	division = this.division.getValue();
    	section = this.section.getValue();
    	searchstatus = this.searchstatus.getValue();
  		projectType = this.projectType.getValue();
  		 
    	document.location.href = '/project/ExportProjectToExcel?fiscalyear='+fiscalyear +'&division='+division +'&section='+section+'&status='+status+'&projectType='+projectType;
    	
    	 
	},
	initComponent: function() {
		var main = this;
		
		main.editProject = new projects.AddProject( );
		
		main.showProject = new Ext.window.Window({
			width : 500,
			height : 550 ,
		    layout: 'fit',
		    closeAction : 'hide' ,
		    plain : true,
		    modal : true,
		    items : [main.editProject]
		});
		main.editProject.fromWin = main.showProject;
		main.editProject.fromMain = main;
		main.gridProject = new projects.gridProject({
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                        //this.up('form').getForm().loadRecord(records[0]);
                        main.showProject.show();
                        main.editProject.setFormEdit(true);
                        main.editProject.setLoadData(records[0]);
                        
                       
                    }
                }
            }
		});
		main.fiscalyear = new Ext.form.field.Number({
			//anchor: '40%',
	        name: 'search_fiscal_year',
	        fieldLabel: 'ปีงบประมาณ',
	        value : year,
	        maxValue: 2600,
        	minValue: 2553	,
        	columnWidth: .40			
		});
		main.division= new Ext.form.field.ComboBox({
			fieldLabel: 'แผนก/ฝ่าย',
			name : 'search_division', 
		    store: maintenance.listDivision,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '',
		    editable: false	,
		    anchor: '100%',
		    listeners:{
		         scope: this,
		         'select': function (  field,   value,   options ){
		         	main.section.reset();
		         	division = value[0].data.id;
		         	projects.listSection.load({
		         		params : {
		         			division : division
		         		}
		         	});
		         	 
		         }
		    }
		    
		});
		main.section = new Ext.form.field.ComboBox({
			fieldLabel: 'หน่วย/งาน',
			name : 'search_section', 
		    store: projects.listSection,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '',
		    editable: false	,
		    anchor: '100%',  
		    columnWidth: .50
		});
		
		main.searchstatus = new Ext.form.field.ComboBox({
			fieldLabel: 'สถานะ',
			name : 'project_status', 
		    store: projects.listStatus,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '',
		    editable: false	,
		    anchor: '100%'  ,
		    columnWidth: .50
		}); 
		
		main.search_button = new Ext.Button({
			text     : 'ค้นหา',
			width : 120,
			listeners: {
		        click: function() {
		        	main.loadDataSearch();     	
		            
			     }  
		      
		    }
					
		});
		
		main.exportExcel_button = new Ext.Button({
			text     : 'บันทึก เป็น Excel',
			width : 120,
			listeners: {
		        click: function() {
		        	main.exportToExcel();     	
		            
			     }  
		      
		    }
					
		});
		
		main.menu_add = new Ext.Button({
			text : 'เพิ่ม/ลบ รายการ',
			width : 120,
			listeners : {
				click : function(){
					//alert("เพิ่มรายหาร");
					window.location = '/project';
					main.editProject.setFormEdit(false);
					main.editProject.getForm().reset();
					main.showProject.show();
				}
			}
		});
		main.addProjectBtn = new Ext.Button({
			text : 'เพิ่ม รายการ',
			width : 120,
			listeners : {
				click : function(){
					//alert("เพิ่มรายหาร");
					 
					main.editProject.setFormEdit(false);
					main.editProject.getForm().reset();
					main.showProject.show();
				}
			}
		});
		main.menu_summary = new Ext.Button({
			text : 'สรุปรายการตามกลุ่มงาน',
			width : 120,
			listeners : {
				click : function() {
					window.location = '/project/summary';
				}
			}
		});
		
		main.projectType = new Ext.form.field.ComboBox({
			fieldLabel: 'ประเภท',
			name : 'searchProjectType',
		    store: projects.listProjectType,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '*',
		    editable: false	,
		    anchor: '100%',
		     
		    labelWidth : 70,
		    blankText :'กรุณาเลือกประเภทโครงการ',
		    columnWidth: .60 ,
		    labelStyle : 'padding: 3px 0px 0px 10px'
		});
		
		main.search = new Ext.form.Panel({
			border : false,
			layout:'column',
			items : [
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
					bodyStyle: {
					    //background: '#ffc',
					    padding: '0px 10px'
					},
		    		columnWidth: .50,
		    		items : [
		    		{
		    			layout : 'column',
		    			border : false,
		    			anchor : '100%',
		    			items : [ main.fiscalyear,main.projectType ]
		    		},main.division
		    		
		    		]
					//items : [main.fiscalyear,main.division ]
				} ,
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
					bodyStyle: {
					    //background: '#ffc',
					    padding: '0px 10px'
					},
		    		columnWidth: .50,
					items : [  main.searchstatus,main.section ]
				} 
				
			 ],
			 dockedItems :[
			  
			 {
				xtype :'toolbar',
				dock : 'bottom',
				ui : 'footer',
				layout : {
					pack : 'center'
				},
				items : [
					main.addProjectBtn ,
					main.search_button,
					main.exportExcel_button
				]
			}]	
		});
		
		Ext.apply(this, {
			bodyPadding: 10,
			dockedItems: [{
            	itemId: 'toolbar',
            	xtype: 'toolbar',
            	items : [ main.menu_add,main.menu_summary  ]
            } ],
			items : [main.search,main.gridProject ]  
		});
		
		projects.ListProject.superclass.initComponent.apply(this, arguments);
	}
});