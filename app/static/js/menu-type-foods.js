new Vue({

    el: '#app',

    data: {
        type_sha_id:'',
        search_keyword: '',
        dialogFormVisible_add_foods: false,
        del_check_visible: false,
        dialogFormVisible: false,
        formLabelWidth: '150px',
        dlg_title: '应用信息',
        form: {},
        delItem: {},//要被删除的
        apiUrl: '/api/v1.0/food-type',
        apiFood: '/api/v1.0/food',
        items: [{'sql_id': 1}],
        un_select_items: [],
        len: 0,
        unit_options: [{ //单位选项
            value: '份',
            label: '份'
        }, {
            value: '瓶',
            label: '瓶'
        }],
    },
    mounted: function () {

        console.log('mounted');
        this.type_sha_id = $("#hidden_type_sha_id").text();

        console.log(this.type_sha_id);


        this.getFoods(this.type_sha_id);
    },


    methods: {

        //归类物品
        CloseDlg: function () {
            this.dialogFormVisible_add_foods = false;
        },
        onCreateDialog_add_foods: function () {
            this.dialogFormVisible_add_foods = true;

            this.getUNSelectFoods(this.type_sha_id);
        },

        switchChange: function (row) {
            console.log(row.states);

            if (row.states == 1) {
                row.states = 0;
            } else {
                row.states = 1;
            }

            this.updateStates(row.sha_id, row.states);
        },

        getUNSelectFoods: function (type_sha_id) {//获取未分类物品
            var vm = this;
            $request.get(vm.apiUrl + '/un/' + type_sha_id, null, function (data) {

                vm.un_select_items = data.value;
                return vm.un_select_items;
            }, function (error_data) {
                console.log(error_data);
            })

        },
        switchType: function (row) {
            //进行归类
            if (row.flag == 1) {
                row.flag = 0;
                this.delTypeFoods(row.m_sha_id);
            } else {
                row.flag = 1;

                this.addTypeFoods(row.sha_id, this.type_sha_id);
            }
        }
        ,
        delTypeFoods: function (m_sha_id) {
        //从该分类中删除
              var vm = this;

              $request.del(this.apiUrl + '/' + m_sha_id, null, function (data) {
                console.log(data);
                vm.$message(data.msg);
                vm.getUNSelectFoods(vm.type_sha_id); //重新获取数据
                vm.getFoods(vm.type_sha_id);
            }, function (error_data) {
                console.log(error_data);
                vm.$message.error(error_data.msg.substring(0, 120));
            })
          }
        ,

        addTypeFoods: function (food_sha_id, menuType_sha_id) {

            var vm = this;

            var temp = {};
            temp.menu_sha_id = menuType_sha_id;
            temp.foods_sha_id = food_sha_id;

            $request.post(this.apiUrl, temp, function (data) {
                var json_target = new JSONFormat(JSON.stringify(data), 4).toString();
                console.log(json_target);
                vm.getUNSelectFoods(vm.type_sha_id); //重新获取数据
                vm.getFoods(vm.type_sha_id);
                vm.$message('添加成功');


            }, function (error_data) {
                var json_target = new JSONFormat(JSON.stringify(error_data), 4).toString();
                vm.$message.error(error_data.msg.substring(0, 120));
            });
        },

        //

        updateStates: function (sha_id, state) {
            //更新状态

            var vm = this;
            $request.get(vm.apiFood + '/' + sha_id + '/' + state, null, function (data) {
                vm.$message(data.msg);

            }, function (error_data) {
                vm.$message.error(error_data.msg.substring(0, 120));
            })

        },

        dlgOk: function (form) {
            var vm = this;
            console.log(form.app_id);
            var temp = {};
            temp.title = form.title;
            temp.food_index = form.food_index;
            temp.description = form.description;
            temp.total_num = form.total_num;
            temp.unit = form.unit;
            temp.discount_price = form.discount_price;
            temp.price = form.price;

            if (form.edit == 'add') {

                console.log('添加');
                $request.post(this.apiFood, temp, function (data) {
                    var json_target = new JSONFormat(JSON.stringify(data), 4).toString();
                    console.log(json_target);
                     vm.getFoods(vm.type_sha_id); //重新获取数据
                    vm.$message('添加成功');
                    vm.dialogFormVisible = false;

                }, function (error_data) {
                    var json_target = new JSONFormat(JSON.stringify(error_data), 4).toString();
                    vm.$message.error(error_data.msg.substring(0, 120));
                });

            } else if (form.edit == 'modify') {
                temp.sha_id = form.sha_id;
                console.log('修改');
                console.log(temp.sha_id);
                $request.put(this.apiFood + '/' + temp.sha_id, temp, function (data) {
                    var json_target = new JSONFormat(JSON.stringify(data), 4).toString();
                    console.log(json_target);
                     vm.getFoods(vm.type_sha_id); //重新获取数据
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
                food_index: 100
            };
        }
        ,
        showCheckDel: function (item) {
            this.del_check_visible = true;
            this.delItem = item;
        }
        ,
        onEdit: function (form) { //编辑
            this.dialogFormVisible = true;
            console.log(form);
            this.form.sha_id = form.sha_id;
            this.form.title = form.title;
            this.form.food_index = form.food_index;
            this.form.description = form.description;
            this.form.total_num = form.total_num;
            this.form.unit = form.unit;
            this.form.discount_price = form.discount_price;
            this.form.price = form.price;

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
                vm.getFoods(); //重新获取数据
            }, function (error_data) {
                console.log(error_data);
                vm.$message.error(error_data.msg.substring(0, 120));
            })
        },

        getFoods: function (type_sha_id) {
            var vm = this;
            $request.get(vm.apiUrl + '/' + type_sha_id, null, function (data) {

                vm.len = data.value.length;
                console.log(data.value);
                // var _apps = new Array();
                //  var apps = data.value.apps;
                // for (index in apps) {
                //     //console.log(index)
                //     //   console.log(data.value[index].app_name)
                //     var temp = {};
                //     temp.id = apps[index].id;
                //
                //     temp.app_name = apps[index].app_name;
                //     temp.value = apps[index].app_name;
                //     temp.app_sql_url = '<a href="/app-sql/' + apps[index].app_id + '">' + apps[index].app_name + '</a>';
                //     temp.app_id = apps[index].app_id;
                //     temp.test_appid = apps[index].test_appid;
                //     temp.app_secretkey = apps[index].app_secretkey;
                //     temp.test_secretkey = apps[index].test_secretkey;
                //     _apps.push(temp);
                // }
                //
                // console.log(_apps);
                // vm.items = _apps;

                vm.items = data.value;
                return data.value;
            }, function (error_data) {
                console.log(error_data);
            })
        }


    }

})