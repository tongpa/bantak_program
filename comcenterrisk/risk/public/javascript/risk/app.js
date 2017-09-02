Ext.Loader.setConfig({enabled: true});
//Ext.Loader.setPath('Ext.ux', '/ux');

Ext.Loader.setPath('Ext.ux', '/javascript/extjs/examples/ux');
Ext.Loader.setPath('risks', '/javascript/risk');
Ext.require([
             
             'Ext.form.*',
             'Ext.layout.container.Column',
             'Ext.ux.form.MultiSelect',
             'Ext.ux.form.ItemSelector',
             'Ext.tip.QuickTipManager',
             'Ext.ux.ajax.JsonSimlet',
             'Ext.ux.ajax.SimManager',             
             'Ext.window.MessageBox'
             
         ]);
 
Ext.application({
    name: 'risks',
    launch: function() {
    	Ext.tip.QuickTipManager.init();
     
    	var listRisk  = Ext.create('risks.view.ListRisk', {
    		level : level, 
    		width : 900,
    		title : 'รายการอุบัติการณ์'
    	}); 
   	
    	var addRisk  = Ext.create('risks.view.AddRisk', {
    		width : 900,
    		 
    		title : 'รายงานอุบัติการณ์'
    	}); 
    	
    	var listResponse = Ext.create('risks.view.ListResponsible',{
    		width : 900,
    		title : 'รายการรับ/ตอบกลับ'
    	});
    	
    	
    	var reportRisk   = new Ext.form.Panel({
 			title : 'สรุปอุบัติการณ์',
 			height : 520 ,
			items:[
				{
					html:"<br>&nbsp;&nbsp;1.<a href='/risk/report1'  target='_blank'> สรุปรายงานอุบัติการณ์/ภาวะไม่พึงประสงค์</a>",
					xtype : "panel",
					border : false					
				},
				{
					html:"<br>&nbsp;&nbsp;2.<a href='/risk/report2' target='_blank'> จำนวนหน่วยงานที่ส่งรายงานอุบัติการณ์/ความเสี่ยง</a>",
					xtype : "panel",
					border : false					
				},
				{
					html:"<br>&nbsp;&nbsp;3.<a href='/risk/report3' target='_blank'> สรุปการนำส่งและการตอบกลับ ข้อมูลความเสี่ยงอุบัติการณ์ ไปยัง<b> หน่วยงาน </b>ที่เกี่ยวข้อง</a>",
					xtype : "panel",
					border : false					
				}
				,
				{
					html:"<br>&nbsp;&nbsp;4.<a href='/risk/report4' target='_blank'> สรุปการนำส่งและการตอบกลับ ข้อมูลความเสี่ยงอุบัติการณ์ ไปยัง<b> ทีมคร่อม </b>ที่เกี่ยวข้อง</a>",
					xtype : "panel",
					border : false					
				},
				{
					html:"<br>&nbsp;&nbsp;5.<a href='/risk/report5' target='_blank'> รายงานอุบัติการณ์ของ <b> ทีมคร่อม </b>ที่เกี่ยวข้อง</a>",
					xtype : "panel",
					border : false					
				}
				,
				{
					html:"<br>&nbsp;&nbsp;6.<a href='/risk/report6' target='_blank'> รายงานความทันเวลาในการจัดการ/ตอบกลับ <b>ทางกายภาพ</b> ของ  <b> หน่วยงาน </b>ที่เกี่ยวข้อง</a>",
					xtype : "panel",
					border : false					
				},
				{
					html:"<br>&nbsp;&nbsp;7.<a href='/risk/report7' target='_blank'> รายงานความทันเวลาในการจัดการ/ตอบกลับ <b>ทางกายภาพ</b> ของ  <b> ทีมคร่อม </b>ที่เกี่ยวข้อง</a>",
					xtype : "panel",
					border : false					
				},
				{
					html:"<br>&nbsp;&nbsp;8.<a href='/risk/report8' target='_blank'> รายงานความทันเวลาในการจัดการ/ตอบกลับ <b>ทางคลินิก</b> ของ  <b> หน่วยงาน </b>ที่เกี่ยวข้อง</a>",
					xtype : "panel",
					border : false					
				},
				{
					html:"<br>&nbsp;&nbsp;9.<a href='/risk/report9' target='_blank'> รายงานความทันเวลาในการจัดการ/ตอบกลับ <b>ทางคลินิก</b> ของ  <b> ทีมคร่อม </b>ที่เกี่ยวข้อง</a>",
					xtype : "panel",
					border : false					
				}
				
			]
		});
    	
    	
    	/* ไม่ได้ใช้แล้ว
    	if(level == 0){
    		reportRisk.setVisible(false);//มองไม่เห็นหน้า report
    	}else
    	{
    		if( level == 1){
    			listResponse.setVisible(false);//มองไม่เห็นหน้า ตอบ
    		}
    	}*/
    	if( level == 1){
			listResponse.setVisible(false);//มองไม่เห็นหน้า ตอบ
		} 
    	 
    	
    	addRisk.loadStore();
    	addRisk.forAnonymousUser();
    	listRisk.loadStore();
    	listResponse.loadStore();
    	
    	Ext.create('Ext.tab.Panel',{
    		renderTo : 'maintenance-app',
    		items : [ addRisk,listRisk,listResponse,reportRisk ]
    	});
    	
     
    	
    	//debugger;
    }
});