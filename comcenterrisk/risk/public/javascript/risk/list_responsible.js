Ext.define('risks.gui.StartDateResp',{
	extend : 'Ext.form.field.Date',
	alias : 'risk.startDateResp',
	fieldLabel : 'วันที่เริ่ม',
	name :'startdtresp',
	id: 'startdtresp',
    vtype: 'daterange',
    format: 'd/m/Y',
    endDateField: 'enddtresp'
});

Ext.define('risks.gui.StopDateResp',{
	extend : 'Ext.form.field.Date',
	alias : 'risk.stopDateResp',
	fieldLabel : 'วันที่สิ้นสุด',
	name: 'enddtresp',
    id: 'enddtresp',
    vtype: 'daterange',
    format: 'd/m/Y',
    startDateField: 'startdtresp'
});
Ext.define('risks.gui.RiskStatusResp',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.riskStatusResp',
	name : 'risk_level_resp',
	fieldLabel: 'สถานะ',
	//store: risks.listRiskStatus,
    queryMode: 'local',
    displayField: 'name',
    valueField: 'id'	,		     
    editable: false	,
    anchor: '100%',
    allowBlank: true, 
    value : "",
    blankText :'กรุณาเลือกสถานะ' 
});


Ext.define('risks.gui.GridRisksResp',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridRisksResp',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = Ext.data.StoreManager.lookup('listRiskRespStore');
    	this.columns =  [
       		{header: 'risk id', dataIndex: 'risk_management_id',width : 40  },      
       		{header: 'วันที่รายงาน', dataIndex: 'report_date' ,xtype: 'datecolumn', format: 'd-m-Y'},
       		{header: 'หน่วยที่รายงาน',  dataIndex: 'risk_section',width : 120},
       		{header: 'รายละเอียด',  dataIndex: 'risk_detail',width : 200},
       		
       		{header: 'ประเภท',  dataIndex: 'risk_program_group',width : 120},
       		{header: 'ด้าน/โปรแกรม',align: 'right', dataIndex: 'risk_program_detail',width : 250 },
       		{header: 'ระดับ',align: 'right', dataIndex: 'risk_level' ,width : 60 } 
		    	        ] ;
		    	
    	this.callParent();
	}
});


Ext.define('risks.view.ListResponsible', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listResponsible',
    level : 0,
    loadStore :function(){
    	
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
        risks.listRiskRespStore.load({
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
    	
    	main.showProject = Ext.create('risks.gui.ShowDetailRisk',{title:'รายการ',fromMain:this,level:level } );
    	
    	
    	main.startDate =    Ext.create('risks.gui.StartDateResp', {anchor : '70%'});
    	main.stopDate =     Ext.create('risks.gui.StopDateResp', {anchor : '70%'});
    	main.riskSection =  Ext.create('risks.gui.RiskSection', {anchor : '100%',store:risks.listRiskSection});
    	main.searchJobId=   Ext.create('risks.gui.SearchJobId', {anchor : '70%'});
    	main.riskProgramDetail = Ext.create('risks.gui.RiskProgramDetail', {anchor : '100%',store:risks.listProgramDetail});
    	main.riskStatus=   Ext.create('risks.gui.RiskStatusResp', {anchor : '100%', disabled : true});
    	
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
    	
    	main.search =    Ext.create('risks.gui.SearchButton', {text     : 'ค้นหา',
    		listeners: {  click: function() { main.loadDataSearch();  }	 }
    	});
    	
    	main.reset =    Ext.create('risks.gui.ResetButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset();main.riskSection.setValue(parseInt(sectionid));  }	 }
    	});
    	
    	
    	main.riskGrid =  Ext.create('risks.gui.GridRisksResp', {anchor : '100%',
    		title : 'รายงานอุบัติการณ์',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                         
                        main.showProject.show();
                        main.showProject.setLoadData(records[0]);
                        main.showProject.setbuttonShowAns();
                        
                        main.showProject.setTitle('รายการ ' + records[0].data.risk_management_id);
                        main.riskGrid.getSelectionModel().deselectAll();
                        
                       
                    }
                }
            }
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
				} ,items : [ main.reset,  main.search  ]
			}]  
			
		});
    	
    	this.items = [ main.layout1,main.riskGrid  ];
    	 
    	
    	this.callParent();
    }

});