Ext.define('coms.gui.ComId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'coms.comId',
	name :'computers_id',
	value : ''
});

Ext.define('coms.gui.detailComs',{
	 extend : 'Ext.form.field.TextArea',
	//extend : 'Ext.form.field.Text',
	alias : 'coms.detailComs',
	name : 'detail',
	fieldLabel: 'รายละเอียด',
	maxHeight : 80,
	height : 70,
	 
	grow      : false
});


Ext.define('coms.gui.nameComs',{
	 extend : 'Ext.form.field.Text',
	//extend : 'Ext.form.field.Text',
	alias : 'coms.namecoms',
	name : 'detail',
	fieldLabel: 'ชื่ออุปกรณ์',
	 
	 
	grow      : false
});


Ext.define('coms.gui.localComs',{
	 extend : 'Ext.form.field.TextArea',
	//extend : 'Ext.form.field.Text',
	alias : 'coms.localComs',
	name : 'location',
	fieldLabel: 'ที่ตั้ง',
	maxHeight : 80,
	height : 70,
	 
	grow      : false
});

Ext.define('coms.gui.comTypes',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'coms.comTypes',
	name : 'computer_types_id',
	fieldLabel: 'ประเภท',
	queryMode: 'local',
	forceSelection: true, 
	editable: false	,
    anchor: '100%',
    allowBlank: false, 
    blankText :'กรุณาเลือกประเภท',
    displayField: 'name',
     
    valueField: 'id'	
});


Ext.define('coms.gui.section',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'coms.section',
	name : 'risk_section_id',
	fieldLabel: 'หน่วยบริการ',
	queryMode: 'local',
	forceSelection: true, 
	editable: false	,
    anchor: '100%',
    allowBlank: false, 
    blankText :'กรุณาเลือกหน่วยบริการ',
    displayField: 'name',
     
    valueField: 'id'	
});


Ext.define('coms.gui.BtClose',{
	extend : 'Ext.Button',
	alias : 'coms.bt.Close', 
	html : '<b>ปิด</b>',
	scale   : 'large',
	width : 120,
	fromWin : null,
	listeners : {
		click : function (){
			if( this.fromWin != null ){
				this.fromWin.hide();
			}
		}
	}
	
});


Ext.define('coms.view.AddCom', {
    extend: 'Ext.form.Panel',
    alias: 'coms.addCom',
    fromWin : null,
    fromMain : null,
    level : 0,
    record : null,
    loadStore :function(){
    	
    	
    	form = this; 
    	risks.listRiskSection.load( );
    	coms.listComputerTypes.load();
    	 
    } ,
    setbuttonShowAns:function(){
    	 
    	 
    },
    setLoadData :function(record){
		form = this;
		this.record = record;
		
		form.getForm().reset();
		 
		
	} ,
    initComponent: function() {
    	var main = this;
     
    	main.comId = Ext.create('coms.gui.ComId');
    	
    	main.detailComs = Ext.create('coms.gui.detailComs', {anchor : '100% -47' });    	
    	main.localComs = Ext.create('coms.gui.localComs', {anchor : '100% -47' });    	
    	main.nameComs = Ext.create('coms.gui.nameComs', {anchor : '100% -47' });    	
    	
   
    	main.comTypes = Ext.create('coms.gui.comTypes', {anchor : '100%',store:coms.listComputerTypes});
    	main.section = Ext.create('coms.gui.section' , {anchor : '100%',store:risks.listRiskSection});  
    	
    	
    	main.save = new Ext.Button({
			//text     : 'บันทึก',
    		html : '<b>บันทึก</b>',
			scale   : 'large',
			width : 120,
			listeners: {
		        click: function() {
		        	valid = this.up('form').getForm().isValid();
		        	 
		        	if(valid){ 		        	 
				           main.getForm().submit({
				                url: '/computer/saveComputer',
				                waitMsg: 'Please waiting...',
				                success: function(fp1, o) {
				                	 
				                	Ext.Msg.alert('บันทึก', 'บันทึกเสร็จเรียบร้อย.' );
				                	main.getForm().reset();
				                	
				                	//set default combobox section
				                	if(main.level == 0)
				                	{
				                		form.riskSection.setValue(parseInt(sectionid));
				                	}
				                	
				                	if( main.fromWin != null ){
										main.fromWin.hide();
									}
									if(main.fromMain != null){
										main.fromMain.loadDataSearch();
									}	  
						       	}
					       });  
		        	}
		        	else{
		        		alert("ตรวจสอบข้อมูลอีกครั้ง ต้องไม่มีข้อมูลว่าง");
		        	}
			     }  
		       
		    }
					
		});
    	
    	this.items = [
    	              main.comId,
    	              main.nameComs,
    	              main.comTypes,
    	              main.section,
    	              main.detailComs,
    	              main.localComs    	            
    	             
    	              ];
   
    	this.dockedItems = [{
            dock: 'bottom',
            xtype: 'toolbar',
            layout : {
				pack : 'center'
			},
			//ui : 'footer',
            items: [
                    	main.save
                   ]
        }];
    	
    	this.callParent();
    }
});

