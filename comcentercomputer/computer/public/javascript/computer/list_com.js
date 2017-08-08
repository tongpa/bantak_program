


Ext.define('coms.gui.GridComs',{
	extend : 'Ext.grid.Panel',
	alias : 'coms.gridcoms',
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