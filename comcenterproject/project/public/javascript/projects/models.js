Ext.regModel('namevalue', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  
    ]
});

Ext.regModel('namevalue1', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' },
        {name: 'other' }   
    ]
});

Ext.regModel('groupByDivision',{
	fields : [
		{name : 'division'},
		{name : 'allBudget'}
		
	]
});
 
Ext.regModel('projectsmodel',{
	fields: [
		{ name: 'project_id'},
		{ name: 'project_name'},
		{ name: 'detail'},
		{ name: 'project_budget'},
		{ name: 'user_name'},
		{ name: 'project_type'},
		{ name: 'project_type_id'},
		{ name: 'division_id'},
		{ name: 'division'},
		{ name: 'department_id'},
		{ name: 'department'},
		{ name: 'section_id'},
		{ name: 'section'},
		{ name: 'project_status_id'},
		{ name: 'project_status'},
		{ name: 'projectType'},
		{ name: 'fiscal_year'},
		{ name: 'budget_other'},
		{ name: 'budget_other_from'},
		{ name: 'maintenance_funds_budget'},		
		{ name: 'start_date',type:'date' , dateFormat: 'Y-m-d H:i:s' },
		{ name: 'stop_date',type:'date' , dateFormat: 'Y-m-d H:i:s' },
		{ name: 'plantype'},
		{ name: 'plantype_id'},
		{ name: 'allBudget'}
		
		
	]
});


Ext.regModel('revenueGroupBy',{
	fields : [
		{name : 'group'},
		{name : 'subgroup'},
		{name : 'estimate'},
		{name : 'fiscal_year'},
		{name : 'revenue_list_id'},
		{name : 'revenue_sub_list_id'}
	]
});

Ext.regModel('expensesGroupBy',{
	fields : [
		{name : 'group'},
		{name : 'subgroup'},
		{name : 'estimate'},
		{name : 'fiscal_year'},
		{name : 'expenses_list_id'},
		{name : 'expenses_sub_list_id'}
	]
});

Ext.regModel('revenuemodel',{
	fields : [
		{name : 'revenue_id'},
		{name : 'revenue_list'},
		{name : 'revenue_sub_list'},
		{name : 'fiscal_year'},
		{name : 'estimate'},
		{name : 'detail'},
		{name : 'income_other'},
		{name : 'revenue_list_name'},
		{name : 'revenue_sub_list_name'} 
	]
});
Ext.regModel('expensesmodel',{
	fields : [
		{name : 'expenses_id'},
		{name : 'expenses_list'},
		{name : 'expenses_sub_list'},
		{name : 'fiscal_year'},
		{name : 'estimate'},
		{name : 'detail'},
		{name : 'income_other'},
		{name : 'expenses_list_name'},
		{name : 'expenses_sub_list_name'} 
	]
});

Ext.namespace("maintenance");
Ext.namespace("projects");
Ext.namespace("revenue");
﻿Ext.namespace("expenses");
﻿Ext.namespace("books");
maintenance.listType =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/maintenance/listMaintenaceType',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

maintenance.listDivision =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/maintenance/listDivision',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

projects.listProjectType = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/project/listProjectType',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

projects.listSection = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/project/listSection',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

projects.listStatus = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/project/listStatus',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

projects.listProjectStore = new Ext.data.Store({
	model : 'projectsmodel',
	storeId:'listProjectStore',
	proxy : {
		type: 'ajax',
		url : '/project/listProject',
		reader : {
			type: 'json',
			root: 'root'
		}
	},
	autoLoad : false
});

projects.sumProjectByDivisionStore = new Ext.data.Store({
	model : 'projectsmodel',
	storeId:'sumProjectByDivisionStore',
	proxy : {
		type: 'ajax',
		url : '/project/listProject',
		reader : {
			type: 'json',
			root: 'root'
		}
	},
	groupField: 'division',
	autoLoad : false
});
projects.showGraphByDivisionStore = new Ext.data.Store({
			fields: [
			    	{name: 'division' }  ,
			         {name: 'allBudget' }  ,
			         {name: 'budget' },
			         {name: 'maintenance_funds_budget' },
			         {name: 'budget_other_from' },
			         {name : 'งบประมาณ'},
			         {name : 'งบประมาณอื่น'},
			         {name : 'เงินบำรุง'}
			    ] ,
			proxy : {
				type: 'ajax',
				url : '/project/showGraphByDivision',
				reader : {
					type: 'json',
					root: 'root'
				}
			},
			autoLoad : false
		});
 
revenue.listDetail =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/revenue/listDetailAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

 revenue.listsSubDetail =   new Ext.data.Store({
	model : 'namevalue1',
	proxy: {
        type: 'ajax',
        url : '/revenue/listSubDetailAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

revenue.listSearchRevenue =   new Ext.data.Store({
	model : 'revenuemodel',
	storeId:'listSearchRevenue',
	proxy: {
        type: 'ajax',
        url : '/revenue/showAllRevenue',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
 
});

revenue.listGroupRevenue =   new Ext.data.Store({
	model : 'revenueGroupBy',
	storeId:'listGroupRevenue',
	sorters: [
        {
            property : 'revenue_list_id',
            direction: 'ASC'
        },
        {
            property : 'revenue_sub_list_id',
            direction: 'ASC'
        }
    ],
	proxy: {
        type: 'ajax',
        url : '/revenue/listGroupRevenue',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    groupField: 'group',
    autoLoad: false
});

revenue.showGraphRevenue = new Ext.data.Store({
			fields: [
			    	{name: 'revenue_list_name' }  ,
			         {name: 'sum_estimate' }   
			    ] ,
			proxy : {
				type: 'ajax',
				url : '/revenue/showGraphRevenue',
				reader : {
					type: 'json',
					root: 'root'
				}
			},
			autoLoad : false
		});
expenses.listDetailExpenses  =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/expenses/listDetailAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
expenses.listsSubDetailExpenses =   new Ext.data.Store({
	model : 'namevalue1',
	proxy: {
        type: 'ajax',
        url : '/expenses/listSubDetailAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

expenses.listSearchExpenses = new Ext.data.Store({
	model : 'expensesmodel',
	storeID:'listSearchExpenses',
	proxy: {
		type: 'ajax',
		url : '/expenses/showAllExpenses',
		reader : {
			type: 'json',
			root : 'root'
		},
	autoload : false
	}
	
});

expenses.listGroupExpenses =   new Ext.data.Store({
	model : 'expensesGroupBy',
	storeId:'listGroupExpenses',
	sorters: [
        {
            property : 'expenses_list_id',
            direction: 'ASC'
        },
        {
            property : 'expenses_sub_list_id',
            direction: 'ASC'
        }
    ],
	proxy: {
        type: 'ajax',
        url : '/expenses/listGroupExpenses',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    groupField: 'group',
    autoLoad: false
});
expenses.showGraphExpenses = new Ext.data.Store({
	fields: [
	    	{name: 'expenses_list_name' }  ,
	         {name: 'sum_estimate' }   
	    ] ,
	proxy : {
		type: 'ajax',
		url : '/expenses/showGraphExpenses',
		reader : {
			type: 'json',
			root: 'root'
		}
	},
	autoLoad : false
});
 generateData = function(n, floor){
        var data = [], i;
        for (i = 0; i < (n || 6); i++) {
            data.push({
                division: '',
                allBudget: 1+i,
                budget: 2+i,
                maintenance_funds_budget: 3+i ,
                budget_other_from:4+i
            });
        }
        return data;
    };
  
/** books*/
    
    Ext.regModel('bookmodel',{
    	fields: [
    		{ name: 'book_id'},
    		{ name: 'book_number'},
    		{ name: 'book_at'},
    		{ name: 'book_recive',type:'date' , dateFormat: 'Y-m-d H:i:s'},
    		{ name: 'book_from'},
    		{ name: 'book_to'},
    		{ name: 'book_detail'},
    		{ name: 'book_operations'},
    		{ name: 'book_remark'},
    		//{ name: 'create_date',type:'date' , dateFormat: 'Y-m-d H:i:s'},
    		//{ name: 'update_date',type:'date' , dateFormat: 'Y-m-d H:i:s'},
    		{ name: 'activate'},
    		{ name: 'book_type'} , 
    		{ name: 'book_type_name'} ,
    		{ name: 'book_file'}  
    		    
             
            
    		
    	]
    });
    
    books.listBookType = new Ext.data.Store({
    	model : 'namevalue',
    	proxy: {
            type: 'ajax',
            url : '/books/listBookType',
            reader: {
                type: 'json',
                root: 'root'
            }
        },
        autoLoad: false
    });
    var itemsPerPage = 5;
    books.listBookReciveInStore = new Ext.data.Store({
    	model : 'bookmodel',
    	storeId:'listBookReciveInStore',
    	pageSize: itemsPerPage,
    	proxy : {
    		type: 'ajax',
    		url : '/books/listBooks',
    		reader : {
    			type: 'json',
    			root: 'root'
    		}
    	},
    	autoLoad : false
    });
    
    books.listBookReciveOutStore = new Ext.data.Store({
    	model : 'bookmodel',
    	storeId:'listBookReciveOutStore',
    	pageSize: itemsPerPage,
    	proxy : {
    		type: 'ajax',
    		url : '/books/listBooks',
    		reader : {
    			type: 'json',
    			root: 'root'
    		}
    	},
    	autoLoad : false
    });
    books.listBookSendInStore = new Ext.data.Store({
    	model : 'bookmodel',
    	storeId:'listBookSendInStore',
    	pageSize: itemsPerPage,
    	proxy : {
    		type: 'ajax',
    		url : '/books/listBooks',
    		reader : {
    			type: 'json',
    			root: 'root'
    		}
    	},
    	autoLoad : false
    });
    
    books.listBookSendOutStore = new Ext.data.Store({
    	model : 'bookmodel',
    	storeId:'listBookSendOutStore',
    	pageSize: itemsPerPage,
    	proxy : {
    		type: 'ajax',
    		url : '/books/listBooks',
    		reader : {
    			type: 'json',
    			root: 'root'
    		}
    	},
    	autoLoad : false
    });
    
 projects.showGraphByDivisionStore.loadData(generateData());