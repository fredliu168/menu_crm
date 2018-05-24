new Vue({
    el: '#app',

    data: {
        search_keyword: '',
        del_check_visible: false,
        dialogFormVisible: false,
        formLabelWidth: '120px',
        dlg_title: '应用信息',
        form: {},
        delItem: {},//要被删除的
        apiUrl: '/api/v1.0/menu-type',
        items: [{'sql_id': 1}],
        len: 0
    },

    methods: {


    }
})