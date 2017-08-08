Ext.define('indicator.gui.RiskSection',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'indicator.riskSection',
	name : 'risk_section_id',
	queryMode: 'local',
	forceSelection: true, 
	fieldLabel: 'หน่วยงาน',
	editable: false	,
    anchor: '100%',
    allowBlank: false,   
    blankText :'กรุณาเลือกหน่วยงานที่รายงาน',
    displayField: 'name',
    valueField: 'id'	
});

Ext.define('indicator.gui.Years',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'indicator.Years',
	name : 'years_id',
	queryMode: 'local',
	forceSelection: true, 
	fieldLabel: 'ปี งบ.',
	editable: false	,
    anchor: '100%',
    allowBlank: false,   
    blankText :'กรุณาเลือกปี',
    displayField: 'name',
    valueField: 'id'	
});

Ext.define('indicator.gui.Months',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'indicator.Months',
	name : 'months_id',
	queryMode: 'local',
	forceSelection: true, 
	fieldLabel: 'เดือน',
	editable: false	,
    anchor: '100%',
    allowBlank: false,   
    blankText :'กรุณาเลือกเดือน',
    displayField: 'name',
    valueField: 'id'	
});

Ext.define('indicator.gui.ResetButton',{
	extend : 'Ext.Button',
	alias : 'indicator.resetButton',
	width : 120
});

Ext.define('risks.gui.SearchButton',{
	extend : 'Ext.Button',
	alias : 'risk.searchButton',
	width : 120
});

Ext.define('indicator.gui.GridIndicator',{
	extend : 'Ext.grid.Panel',
	alias : 'indicator.gridIndicator',
	border :false,
	requires: [
         'Ext.grid.plugin.CellEditing',
         'Ext.form.field.Text',
         'Ext.toolbar.TextItem'
     ],
	initComponent: function() {
    	var main = this;
    	this.store = Ext.data.StoreManager.lookup('listIndicatorStore');
    	//this.editing = Ext.create('Ext.grid.plugin.CellEditing');
    	this.editing = Ext.create('Ext.grid.plugin.RowEditing');
    	this.columns =  [
		    	       		//{header: 'risk id', dataIndex: 'indicators_detail_id',width : 40  },      
		    	       	    {header: 'id', dataIndex: 'id',width : 40  },      
		    	       	    
		    	       		{header: 'ตัวชี้วัด',  dataIndex: 'detail',width : 300},
		    	       		{header: 'เป้าหมาย',  dataIndex: 'target',width : 100},
		    	       		{header: 'ตัวชี้วัดประจำเดือน',align: 'right', dataIndex: 'indicator_value',width : 150,field: { type: 'textfield' } } 
		    	        ] ;
		    	
    	this.plugins =  [this.editing];
    	
    	this.callParent();
	}
});


Ext.define('indicator.view.AddIndicator', {
    extend: 'Ext.form.Panel',
    alias: 'risk.addRisk',
    fromWin : null,
    fromMain : null,
    level : 0,
    record : null,
    storeRiskSection: indicator.listAllRiskSection,
    storeYears: indicator.listYearsStore ,
    storeMonth : indicator.listMonthsStore ,
    loadStore : function(){
    	
    	form = this; 
    	if(sectionid ){
    		this.storeRiskSection.load({
    			params:{ section_id : sectionid },
    			 
         		callback: function(records, o, s) {
                    if (s) {
                    	form.riskSection.setValue(parseInt(sectionid));
                    }
            	}
    		
    		});
    		
    		 
    	}
    	else{
    		this.storeRiskSection.load();
    		 
    	}
    	
    	 
    	this.storeYears.load();
    	this.storeMonth.load();
    	
    	form.years.setValue(parseInt(year));
    	form.months.setValue(parseInt(month));
    	
    	indicator.listIndicatorStore.load({
			params:{ riskSection : sectionid ,
							year : null,
							months_id: null	},
			 
     		callback: function(records, o, s) {
                if (s) {
        
                }
        	}
		
		}); 
    	
    },
    loadDataSearch: function(){
    	
    	var main = this;
    	year = main.years.getValue() ;
    	month = main.months.getValue() ;
    	riskSection = main.riskSection.getValue() ;
		
    	indicator.listIndicatorStore.load({
        	params : {
        		year : year,
        		month : month,
        		riskSection : riskSection 
     		}
        });
    	
    },
    forAnonymousUser : function(){
    	 
    },
    initComponent: function() {
    	var main = this;
    	
    	main.years  = Ext.create('indicator.gui.Years', {anchor : '100%',store:main.storeYears});
    	main.months = Ext.create('indicator.gui.Months', {anchor : '100%',store:main.storeMonth});
    	main.riskSection = Ext.create('indicator.gui.RiskSection', {anchor : '100%',store:main.storeRiskSection});
    	
    	
    	main.riskGrid =  Ext.create('indicator.gui.GridIndicator', {anchor : '100%',
    		//title : ' ',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                    	 
                     /*   main.showProject.show();
                        main.showProject.setLoadData(records[0]);
                      
                        main.showProject.setTitle('รายการ ' + records[0].data.risk_management_id);
                        main.riskGrid.getSelectionModel().deselectAll();
                        
                       */
                    }
                }
            }
         });
    	
    	main.reset =    Ext.create('indicator.gui.ResetButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset(); main.riskSection.setValue(parseInt(sectionid)); }	 }
    	});
    	
    	main.search =    Ext.create('risks.gui.SearchButton', {text     : 'ค้นหา',
    		listeners: {  click: function() { main.loadDataSearch();  }	 }
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
		    		items : [ main.years,main.riskSection   ]
					 
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
					items : [main.months ]
				}   ],
			dockedItems :[{
				xtype :'toolbar',
				dock : 'bottom',
				ui : 'footer',
				layout : {
					pack : 'center'
				},
				items : [main.reset ,main.search 
					
				]
			}]  
			
		});
    	
    	this.items = [ main.layout1,main.riskGrid  ];
    	
    	this.callParent();
    }
});
    
    