Ext.apply(Ext.form.field.VTypes, {
        daterange: function(val, field) {
            var date = field.parseDate(val);

            if (!date) {
                return false;
            }
            if (field.startDateField && (!this.dateRangeMax || (date.getTime() != this.dateRangeMax.getTime()))) {
                var start = field.up('form').down('#' + field.startDateField);
                start.setMaxValue(date);
                start.validate();
                this.dateRangeMax = date;
            }
            else if (field.endDateField && (!this.dateRangeMin || (date.getTime() != this.dateRangeMin.getTime()))) {
                var end = field.up('form').down('#' + field.endDateField);
                end.setMinValue(date);
                end.validate();
                this.dateRangeMin = date;
            }
             
            return true;
        },

        daterangeText: 'วันที่เริ่มต้นต้องน้อยกว่าวันที่สิ้นสุด'
 
    });

Ext.define('risks.gui.StartDate',{
	extend : 'Ext.form.field.Date',
	alias : 'risk.startDate',
	fieldLabel : 'วันที่เริ่ม',
	name :'startdt',
	id: 'startdt',
    vtype: 'daterange',
    format: 'd/m/Y',
    endDateField: 'enddt'
});

Ext.define('risks.gui.StopDate',{
	extend : 'Ext.form.field.Date',
	alias : 'risk.stopDate',
	fieldLabel : 'วันที่สิ้นสุด',
	name: 'enddt',
    id: 'enddt',
    vtype: 'daterange',
    format: 'd/m/Y',
    startDateField: 'startdt'
});

Ext.define('risks.gui.SearchJobId',{
	extend : 'Ext.form.field.Text',
	alias : 'risk.searchJobId',
	name:'search_job_id',
	fieldLabel : 'เลข risk id',
	allowBlank: true
});


Ext.define('risks.gui.RiskProgramGroupCombo',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.riskProgramGroupCombo',
	name : 'risk_program_group',
	fieldLabel: 'ประเภท',
	store: risks.listProgramGroup,
    queryMode: 'local',
    displayField: 'name',
    valueField: 'id'	,		     
    editable: false	,
    anchor: '100%',
    allowBlank: true, 
    blankText :'กรุณาเลือกประเภท'
});


Ext.define('risks.gui.RiskStatus',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.riskStatus',
	name : 'risk_level',
	fieldLabel: 'สถานะ',
	store: risks.listRiskStatus,
    queryMode: 'local',
    displayField: 'name',
    valueField: 'id'	,		     
    editable: false	,
    anchor: '100%',
    allowBlank: true, 
    value : 1,
    blankText :'กรุณาเลือกสถานะ' 
});
 
Ext.define('risks.gui.SearchButton',{
	extend : 'Ext.Button',
	alias : 'risk.searchButton',
	width : 120
});

Ext.define('risks.gui.ResetButton',{
	extend : 'Ext.Button',
	alias : 'risk.resetButton',
	width : 120
});

Ext.define('risks.gui.GridRisks',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridRisks',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = Ext.data.StoreManager.lookup('listRiskStore');
    	this.columns =  [
		    	       		{header: 'risk id', dataIndex: 'risk_management_id',width : 40  },      
		    	       		{header: 'วันที่รายงาน', dataIndex: 'report_date' ,xtype: 'datecolumn', format: 'd-m-Y'},
		    	       		{header: 'หน่วยงาน',  dataIndex: 'risk_section',width : 120},
		    	       		{header: 'ประเภท',  dataIndex: 'risk_program_group',width : 120},
		    	       		{header: 'ด้าน/โปรแกรม',align: 'right', dataIndex: 'risk_program_detail',width : 250 },
		    	       		{header: 'ระดับ',align: 'right', dataIndex: 'risk_level' ,width : 60 },
		    	       		{header: 'สถานะ',align: 'right', dataIndex: 'risk_status' }
		    	        ] ;
		    	
    	this.callParent();
	}
});


Ext.define('risks.gui.ShowDetailRisk',{
	extend : 'Ext.window.Window',
	alias : 'risk.showDetailRisk',
	width : 800,
	height : 550 ,
    layout: 'fit',
    closeAction : 'hide' ,
    plain : true,
    modal : false,
    fromMain : null,
    level : 0,
    showButtonAns : false,
    setbuttonShowAns:function(){
    	 
    	this.showRiskManage.setbuttonShowAns( ); 
    	  
    },
    setLoadData : function(record){
    	this.showRiskManage.setLoadData(record);
    },
    initComponent: function() {
    	var main = this;
    	main.store  = null;
    	if(this.level == 0){ //case level is user get only user
    		 
    		main.store  =  risks.listRiskSection;
    	}
    	else{ //case level is admin get all
    		main.store  =  risks.listAllRiskSection;
    	}
    	
    	
    	main.showRiskManage = Ext.create('risks.view.AddRisk',{
    		storeRiskSection : main.store ,
    		fromWin : main,
    		fromMain : this.fromMain,
    		level : this.level
    	} ); 
    	
     
    	
    	
    	//show and not show button
    	if(this.level == 0){//user
    		main.showRiskManage.forAnonymousUser(); 
    		main.showRiskManage.storeRiskSection = risks.listRiskSection;
    			
    	}
    	
    	this.items = [main.showRiskManage];
    	
    	this.callParent();
    }
});

 
Ext.define('risks.view.ListRisk', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listRisk',
    level : 0,
    loadStore :function(){
    	risks.listProgramGroup.load();
    	risks.listRiskStatus.load();
    	risks.listAllRiskSection.load();
    	
    	this.riskSection.setValue(parseInt(sectionid));
    },
    loadDataSearch : function(){
		var main = this;
		startDate = main.startDate.getValue() ;
		        	
		        	
    	stopDate = main.stopDate.getValue() ;
    	riskSection = main.riskSection.getValue();
    	riskProgramGroup = main.riskProgramGroup.getValue();
    	riskStatus = main.riskStatus.getValue();
    	riskProgramDetail = main.riskProgramDetail.getValue();
    	searchJobId = main.searchJobId.getValue();
    	if(isNaN(riskSection)  )
    	{
    		riskSection = '';
    	}
        risks.listRiskStore.load({
        	params : {
     			startDate : startDate,
     			stopDate : stopDate,
     			riskSection : riskSection,
     			riskProgramGroup : riskProgramGroup,
     			riskStatus : riskStatus,
     			riskProgramDetail : riskProgramDetail,
     			riskJobId : searchJobId
     		}
        });
         
	}, 
    initComponent: function() {
    	var main = this;
    	
    	main.showProject = Ext.create('risks.gui.ShowDetailRisk',{title:'รายการ',fromMain:this,level:level} );
    	
    	main.startDate =    Ext.create('risks.gui.StartDate', {anchor : '70%'});
    	main.stopDate =     Ext.create('risks.gui.StopDate', {anchor : '70%'});
    	main.riskSection =  Ext.create('risks.gui.RiskSection', {anchor : '100%',store:risks.listRiskSection});
    	main.searchJobId=   Ext.create('risks.gui.SearchJobId', {anchor : '70%'});
    	main.riskProgramDetail = Ext.create('risks.gui.RiskProgramDetail', {anchor : '100%',store:risks.listProgramDetail});
    	
    	main.riskStatus=   Ext.create('risks.gui.RiskStatus', {anchor : '100%'});
    	
    	main.riskProgramGroup =   Ext.create('risks.gui.RiskProgramGroupCombo', {anchor : '100%',
			    		listeners:{
					         scope: this,
					         'select': function (  field,   value,   options ){
					         	main.riskProgramDetail.reset();
					         	division = value[0].data.id;
					         	risks.listProgramDetail.load({
					         		params : {
					         			 risk_program_group_id : division
					         		}
					         	});
					         	 
					         }
					    }
    			});
    	 
    	main.riskGrid =  Ext.create('risks.gui.GridRisks', {anchor : '100%',
    		title : 'รายงานอุบัติการณ์',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                    	 
                        main.showProject.show();
                        main.showProject.setLoadData(records[0]);
                      
                        main.showProject.setTitle('รายการ ' + records[0].data.risk_management_id);
                        main.riskGrid.getSelectionModel().deselectAll();
                        
                       
                    }
                }
            }
         });
    	 
    	main.search =    Ext.create('risks.gui.SearchButton', {text     : 'ค้นหา',
    		listeners: {  click: function() { main.loadDataSearch();  }	 }
    	});
    	
    	main.reset =    Ext.create('risks.gui.ResetButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset(); main.riskSection.setValue(parseInt(sectionid)); }	 }
    	});
    	
    	main.layout1 = Ext.create('Ext.Panel',{
			border : false,
			 
			autoWidth : true,
			anchor: '100%',
			layout:'column',
			defaults:{margins:'0 5 5 0'},
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
		    		items : [ main.startDate,main.riskSection,main.riskProgramGroup,main.searchJobId   ]
					 
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
					items : [main.stopDate,main.riskStatus,main.riskProgramDetail ]
				}   ],
			dockedItems :[{
				xtype :'toolbar',
				dock : 'bottom',
				ui : 'footer',
				layout : {
					pack : 'center'
				},
				items : [main.reset,
					  main.search 
				]
			}]  
			
		});
    	
    	this.items = [ main.layout1,    	main.riskGrid ];
    	
    	
    	
    	this.callParent();
    }
    
});