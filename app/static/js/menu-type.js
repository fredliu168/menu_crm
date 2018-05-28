new Vue({

    el: '#app',

    data: {
        search_keyword: '',
        del_check_visible: false,
        dialogFormVisible: false,
        formLabelWidth: '150px',
        dlg_title: '应用信息',
        form: {},
        delItem: {},//要被删除的
        apiUrl: '/api/v1.0/menu-type',
        items: [{'sql_id': 1}],
        len: 0
    },
    mounted: function () {
        this.getMenuTypes();
    },


    methods: {

        dlgOk: function (form) {
            var vm = this;
            console.log(form.app_id);
            var temp = {};
            temp.title = form.title;
            temp.type_index = form.type_index;


            if (form.edit == 'add') {

                console.log('添加');
                $request.post(this.apiUrl, temp, function (data) {
                    var json_target = new JSONFormat(JSON.stringify(data), 4).toString();
                    console.log(json_target);
                    vm.getMenuTypes(); //重新获取数据
                    vm.$message('添加成功');
                    vm.dialogFormVisible = false;

                }, function (error_data) {
                    var json_target = new JSONFormat(JSON.stringify(error_data), 4).toString();
                    vm.$message.error(error_data.msg.substring(0, 120));
                });

            }else if(form.edit =='modify')
            {
                temp.sha_id = form.sha_id;
                console.log('修改');
                console.log(temp.sha_id);
                $request.put(this.apiUrl+'/'+temp.sha_id, temp, function (data) {
                   var json_target = new JSONFormat(JSON.stringify(data), 4).toString();
                    console.log(json_target);
                    vm.getMenuTypes(); //重新获取数据
                    vm.$message('修改成功');
                    vm.dialogFormVisible = false;

                }, function (error_data) {
                    var json_target = new JSONFormat(JSON.stringify(error_data), 4).toString();
                    vm.$message.error(error_data.msg.substring(0, 120));
                });
            }

        }
        ,

        onCreateDialog: function () {
            //创建新app信息
            this.dialogFormVisible = true;
            this.form = {
                ok: '添加',
                edit: 'add',
                type_index :100
            };
        }
        ,
        showCheckDel: function (item) {
            this.del_check_visible = true;
            this.delItem = item;
        }
        ,
        onEdit: function (item) { //编辑
            this.dialogFormVisible = true;
            console.log(item);
            this.form.sha_id = item.sha_id;
            this.form.title = item.title;
            this.form.type_index = item.type_index;
            this.form.ok = '修改';
            this.form.edit = 'modify';
        }
        ,

        onDel: function () {
            var vm = this;
            console.log(this.delItem.sha_id);
            vm.del_check_visible = false;
            console.log('删除');
            $request.del(this.apiUrl + '/' + this.delItem.sha_id, null, function (data) {
                console.log(data);
                vm.$message(data.msg);
                vm.getMenuTypes(); //重新获取数据
            }, function (error_data) {
                console.log(error_data);
                vm.$message.error(error_data.msg.substring(0, 120));
            })
        },

        showMenuFoods:function(row){


              this.$router.push('/menu-type-foods/'+ row.sha_id);
        },

        getMenuTypes: function () {
            var vm = this;
            $request.get(vm.apiUrl, null, function (data) {

                vm.len = data.value.length;
                console.log(data.value);
                var _types = new Array();
                 var types = data.value;
                for (index in types) {

                    var temp = {};
                    temp.id = types[index].id;

                    temp.title = types[index].title;
                    temp.sha_id = types[index].sha_id;
                    temp.foods_url = '<a href="/menu-type-foods/' + types[index].sha_id + '">' + types[index].title + '</a>';
                    temp.type_index = types[index].type_index;

                    _types.push(temp);
                }

                console.log(_types);
                vm.items = _types;

               // vm.items = data.value;
                return vm.items;
            }, function (error_data) {
                console.log(error_data);
            })
        }


    }

})