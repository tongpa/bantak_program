  

Ext.define('risks.gui.GridListRisksInMonth',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridListRisksInMonth',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = Ext.data.StoreManager.lookup('listInMonthStore');
    	
    	function renderTip(val, meta, rec, rowIndex, colIndex, store) {
            meta.tdAttr = 'ddddd"' + val + '"';
            return val;
    };
    
    	this.columns =  [
		    	       		{header: 'risk id', dataIndex: 'risk_management_id',width : 40 },      
		    	       		{header: 'วันที่รายงาน', dataIndex: 'report_date' ,xtype: 'datecolumn', format: 'd-m-Y' ,width : 70 },
		    	       		{header: 'หน่วยงาน',  dataIndex: 'risk_section',width : 120 },
		    	       		{header: 'รายละเอียด',  dataIndex: 'risk_detail',width : 540, 
		                           renderer: renderTip} 
		    	        ] ;
		    	
    	this.callParent();
	}
});

 
 
Ext.define('risks.view.ListRiskInMonth', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listRiskInMonth',
    level : 0,
    loadStore :function(){
    	risks.listInMonth.load(); 
    },
    loadDataSearch : function(){
    	risks.listInMonth.load(); 
	}, 
    initComponent: function() {
    	var main = this;
    	main.riskGrid =  Ext.create('risks.gui.GridListRisksInMonth', {anchor : '100%',
    		title : 'อุบัติการณ์ที่รายงานแล้ว',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                     
                }
            }
         });
    	this.items = [  	main.riskGrid ];
    	this.callParent();
    }
    
});