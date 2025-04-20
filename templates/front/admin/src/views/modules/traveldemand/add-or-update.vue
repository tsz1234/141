<template>
	<div class="addEdit-block">
		<el-form
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="120px"
		>
			<template >
				<el-form-item class="date" v-if="type!='info'" label="开始时间" prop="starttime" >
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.starttime" 
						type="datetime"
						:readonly="ro.starttime"
						placeholder="开始时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item class="input" v-else-if="ruleForm.starttime" label="开始时间" prop="starttime" >
					<el-input v-model="ruleForm.starttime" placeholder="开始时间" readonly></el-input>
				</el-form-item>
				<el-form-item class="date" v-if="type!='info'" label="结束时间" prop="jieshushijian" >
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.jieshushijian" 
						type="datetime"
						:readonly="ro.jieshushijian"
						placeholder="结束时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item class="input" v-else-if="ruleForm.jieshushijian" label="结束时间" prop="jieshushijian" >
					<el-input v-model="ruleForm.jieshushijian" placeholder="结束时间" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="开始站点" prop="kaishizhandian" >
					<el-input v-model="ruleForm.kaishizhandian" placeholder="开始站点" clearable  :readonly="ro.kaishizhandian"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="开始站点" prop="kaishizhandian" >
					<el-input v-model="ruleForm.kaishizhandian" placeholder="开始站点" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="结束站点" prop="jieshuzhandian" >
					<el-input v-model="ruleForm.jieshuzhandian" placeholder="结束站点" clearable  :readonly="ro.jieshuzhandian"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="结束站点" prop="jieshuzhandian" >
					<el-input v-model="ruleForm.jieshuzhandian" placeholder="结束站点" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="使用者编号" prop="shiyongzhebianhao" >
					<el-input v-model="ruleForm.shiyongzhebianhao" placeholder="使用者编号" clearable  :readonly="ro.shiyongzhebianhao"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="使用者编号" prop="shiyongzhebianhao" >
					<el-input v-model="ruleForm.shiyongzhebianhao" placeholder="使用者编号" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="使用者性别" prop="shiyongzhexingbie" >
					<el-input v-model="ruleForm.shiyongzhexingbie" placeholder="使用者性别" clearable  :readonly="ro.shiyongzhexingbie"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="使用者性别" prop="shiyongzhexingbie" >
					<el-input v-model="ruleForm.shiyongzhexingbie" placeholder="使用者性别" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="使用者年龄" prop="shiyongzhenianling" >
					<el-input v-model="ruleForm.shiyongzhenianling" placeholder="使用者年龄" clearable  :readonly="ro.shiyongzhenianling"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="使用者年龄" prop="shiyongzhenianling" >
					<el-input v-model="ruleForm.shiyongzhenianling" placeholder="使用者年龄" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="骑行时长(分钟)" prop="qixingshizhang" >
					<el-input-number v-model="ruleForm.qixingshizhang" placeholder="骑行时长(分钟)" :disabled="ro.qixingshizhang"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="骑行时长(分钟)" prop="qixingshizhang" >
					<el-input v-model="ruleForm.qixingshizhang" placeholder="骑行时长(分钟)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="骑行距离(公里)" prop="qixingjuli" >
					<el-input-number v-model="ruleForm.qixingjuli" placeholder="骑行距离(公里)" :disabled="ro.qixingjuli"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="骑行距离(公里)" prop="qixingjuli" >
					<el-input v-model="ruleForm.qixingjuli" placeholder="骑行距离(公里)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="当日天气" prop="dangritianqi" >
					<el-input v-model="ruleForm.dangritianqi" placeholder="当日天气" clearable  :readonly="ro.dangritianqi"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="当日天气" prop="dangritianqi" >
					<el-input v-model="ruleForm.dangritianqi" placeholder="当日天气" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="当日温度(摄氏度)" prop="dangriwendu" >
					<el-input v-model="ruleForm.dangriwendu" placeholder="当日温度(摄氏度)" clearable  :readonly="ro.dangriwendu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="当日温度(摄氏度)" prop="dangriwendu" >
					<el-input v-model="ruleForm.dangriwendu" placeholder="当日温度(摄氏度)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="当日湿度(%)" prop="dangrishidu" >
					<el-input v-model="ruleForm.dangrishidu" placeholder="当日湿度(%)" clearable  :readonly="ro.dangrishidu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="当日湿度(%)" prop="dangrishidu" >
					<el-input v-model="ruleForm.dangrishidu" placeholder="当日湿度(%)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="当日风速(米/秒)" prop="dangrifengsu" >
					<el-input v-model="ruleForm.dangrifengsu" placeholder="当日风速(米/秒)" clearable  :readonly="ro.dangrifengsu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="当日风速(米/秒)" prop="dangrifengsu" >
					<el-input v-model="ruleForm.dangrifengsu" placeholder="当日风速(米/秒)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="是否工作日" prop="shifougongzuori" >
					<el-input v-model="ruleForm.shifougongzuori" placeholder="是否工作日" clearable  :readonly="ro.shifougongzuori"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="是否工作日" prop="shifougongzuori" >
					<el-input v-model="ruleForm.shifougongzuori" placeholder="是否工作日" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="是否节假日" prop="shifoujiejiari" >
					<el-input v-model="ruleForm.shifoujiejiari" placeholder="是否节假日" clearable  :readonly="ro.shifoujiejiari"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="是否节假日" prop="shifoujiejiari" >
					<el-input v-model="ruleForm.shifoujiejiari" placeholder="是否节假日" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="小时级租赁数量" prop="hourlyrentalquantity" >
					<el-input v-model.number="ruleForm.hourlyrentalquantity" placeholder="小时级租赁数量" clearable  :readonly="ro.hourlyrentalquantity"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="小时级租赁数量" prop="hourlyrentalquantity" >
					<el-input v-model="ruleForm.hourlyrentalquantity" placeholder="小时级租赁数量" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="出行需求量" prop="traveldemand" >
					<el-input v-model.number="ruleForm.traveldemand" placeholder="出行需求量" clearable  :readonly="ro.traveldemand"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="出行需求量" prop="traveldemand" >
					<el-input v-model="ruleForm.traveldemand" placeholder="出行需求量" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="出行频率" prop="travelfrequency" >
					<el-input v-model.number="ruleForm.travelfrequency" placeholder="出行频率" clearable  :readonly="ro.travelfrequency"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="出行频率" prop="travelfrequency" >
					<el-input v-model="ruleForm.travelfrequency" placeholder="出行频率" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan"></span>
					提交
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

	</div>
</template>
<script>
	import { 
		isNumber,
		isIntNumer,
	} from "@/utils/validate";
	export default {
		data() {
			var validateNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isNumber(value)) {
					callback(new Error("请输入数字"));
				} else {
					callback();
				}
			};
			var validateIntNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isIntNumer(value)) {
					callback(new Error("请输入整数"));
				} else {
					callback();
				}
			};
			return {
				id: '',
				type: '',
			
			
				ro:{
					starttime : false,
					jieshushijian : false,
					kaishizhandian : false,
					jieshuzhandian : false,
					shiyongzhebianhao : false,
					shiyongzhexingbie : false,
					shiyongzhenianling : false,
					qixingshizhang : false,
					qixingjuli : false,
					dangritianqi : false,
					dangriwendu : false,
					dangrishidu : false,
					dangrifengsu : false,
					shifougongzuori : false,
					shifoujiejiari : false,
					hourlyrentalquantity : false,
					traveldemand : false,
					travelfrequency : false,
				},
			
				ruleForm: {
					starttime: '',
					jieshushijian: '',
					kaishizhandian: '',
					jieshuzhandian: '',
					shiyongzhebianhao: '',
					shiyongzhexingbie: '',
					shiyongzhenianling: '',
					qixingshizhang: '',
					qixingjuli: '',
					dangritianqi: '',
					dangriwendu: '',
					dangrishidu: '',
					dangrifengsu: '',
					shifougongzuori: '',
					shifoujiejiari: '',
					hourlyrentalquantity: '',
					traveldemand: '',
					travelfrequency: '',
				},

				rules: {
					starttime: [
					],
					jieshushijian: [
					],
					kaishizhandian: [
					],
					jieshuzhandian: [
					],
					shiyongzhebianhao: [
					],
					shiyongzhexingbie: [
					],
					shiyongzhenianling: [
					],
					qixingshizhang: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					qixingjuli: [
						{ validator: validateNumber, trigger: 'blur' },
					],
					dangritianqi: [
					],
					dangriwendu: [
					],
					dangrishidu: [
					],
					dangrifengsu: [
					],
					shifougongzuori: [
					],
					shifoujiejiari: [
					],
					hourlyrentalquantity: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					traveldemand: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					travelfrequency: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
				},
			};
		},
		props: ["parent"],
		computed: {



		},
		components: {
		},
		created() {
		},
		methods: {
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(id,type) {
				if (id) {
					this.id = id;
					this.type = type;
				}
				if(this.type=='info'||this.type=='else'||this.type=='msg'){
					this.info(id);
				}else if(this.type=='logistics'){
					for(let x in this.ro) {
						this.ro[x] = true
					}
					this.logistics=false;
					this.info(id);
				}else if(this.type=='cross'){
					var obj = this.$storage.getObj('crossObj');
					for (var o in obj){
						if(o=='starttime'){
							this.ruleForm.starttime = obj[o];
							this.ro.starttime = true;
							continue;
						}
						if(o=='jieshushijian'){
							this.ruleForm.jieshushijian = obj[o];
							this.ro.jieshushijian = true;
							continue;
						}
						if(o=='kaishizhandian'){
							this.ruleForm.kaishizhandian = obj[o];
							this.ro.kaishizhandian = true;
							continue;
						}
						if(o=='jieshuzhandian'){
							this.ruleForm.jieshuzhandian = obj[o];
							this.ro.jieshuzhandian = true;
							continue;
						}
						if(o=='shiyongzhebianhao'){
							this.ruleForm.shiyongzhebianhao = obj[o];
							this.ro.shiyongzhebianhao = true;
							continue;
						}
						if(o=='shiyongzhexingbie'){
							this.ruleForm.shiyongzhexingbie = obj[o];
							this.ro.shiyongzhexingbie = true;
							continue;
						}
						if(o=='shiyongzhenianling'){
							this.ruleForm.shiyongzhenianling = obj[o];
							this.ro.shiyongzhenianling = true;
							continue;
						}
						if(o=='qixingshizhang'){
							this.ruleForm.qixingshizhang = obj[o];
							this.ro.qixingshizhang = true;
							continue;
						}
						if(o=='qixingjuli'){
							this.ruleForm.qixingjuli = obj[o];
							this.ro.qixingjuli = true;
							continue;
						}
						if(o=='dangritianqi'){
							this.ruleForm.dangritianqi = obj[o];
							this.ro.dangritianqi = true;
							continue;
						}
						if(o=='dangriwendu'){
							this.ruleForm.dangriwendu = obj[o];
							this.ro.dangriwendu = true;
							continue;
						}
						if(o=='dangrishidu'){
							this.ruleForm.dangrishidu = obj[o];
							this.ro.dangrishidu = true;
							continue;
						}
						if(o=='dangrifengsu'){
							this.ruleForm.dangrifengsu = obj[o];
							this.ro.dangrifengsu = true;
							continue;
						}
						if(o=='shifougongzuori'){
							this.ruleForm.shifougongzuori = obj[o];
							this.ro.shifougongzuori = true;
							continue;
						}
						if(o=='shifoujiejiari'){
							this.ruleForm.shifoujiejiari = obj[o];
							this.ro.shifoujiejiari = true;
							continue;
						}
						if(o=='hourlyrentalquantity'){
							this.ruleForm.hourlyrentalquantity = obj[o];
							this.ro.hourlyrentalquantity = true;
							continue;
						}
						if(o=='traveldemand'){
							this.ruleForm.traveldemand = obj[o];
							this.ro.traveldemand = true;
							continue;
						}
						if(o=='travelfrequency'){
							this.ruleForm.travelfrequency = obj[o];
							this.ro.travelfrequency = true;
							continue;
						}
					}
				}
				// 获取用户信息
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						var json = data.data;
					} else {
						this.$message.error(data.msg);
					}
				});
			
			},
			// 多级联动参数

			info(id) {
				this.$http({
					url: `traveldemand/info/${id}`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.ruleForm = data.data;
						//解决前台上传图片后台不显示的问题
						let reg=new RegExp('../../../upload','g')//g代表全部
					} else {
						this.$message.error(data.msg);
					}
				});
			},

			// 提交
			async onSubmit() {
					var objcross = this.$storage.getObj('crossObj');
					if(!this.ruleForm.id) {
						delete this.ruleForm.userid
					}
					await this.$refs["ruleForm"].validate(async valid => {
						if (valid) {
							if(this.type=='cross'){
								var statusColumnName = this.$storage.get('statusColumnName');
								var statusColumnValue = this.$storage.get('statusColumnValue');
								if(statusColumnName!='') {
									var obj = this.$storage.getObj('crossObj');
									if(statusColumnName && !statusColumnName.startsWith("[")) {
										for (var o in obj){
											if(o==statusColumnName){
												obj[o] = statusColumnValue;
											}
										}
										var table = this.$storage.get('crossTable');
										await this.$http({
											url: `${table}/update`,
											method: "post",
											data: obj
										}).then(({ data }) => {});
									}
								}
							}
							
							await this.$http({
								url: `traveldemand/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(async ({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.traveldemandCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
								}
							});
						}
					});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.parent.showFlag = true;
				this.parent.addOrUpdateFlag = false;
				this.parent.traveldemandCrossAddOrUpdateFlag = false;
				this.parent.contentStyleChange();
			},
		}
	};
</script>
<style lang="scss" scoped>
	.addEdit-block {
		padding: 20px 30px;
	}
	.add-update-preview {
		border: 1px solid #BFBFBF;
		padding: 40px 20% 20px 15%;
		background: #fff;
	}
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	.add-update-preview /deep/ .el-form-item {
		border: 0px solid #eee;
		padding: 0;
		margin: 0 0 20px 0;
		display: inline-block;
		width: 80%;
	}
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
		padding: 0 10px 0 0;
		color: #666;
		font-weight: 600;
		width: 120px;
		font-size: 16px;
		line-height: 40px;
		text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 120px;
	}
	.add-update-preview .el-form-item span.text {
		border: 1px solid #ddd;
		border-radius: 0px;
		padding: 5px 10px;
		color: #000000;
		display: block;
		width: 100%;
		font-size: 16px;
		line-height: 24px;
		height: auto;
	}
	
	.add-update-preview .el-input {
		width: 100%;
	}
	.add-update-preview .el-input /deep/ .el-input__inner {
		border: 1px dashed #ababab;
		border-radius: 0px;
		padding: 0 12px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .el-input /deep/ .el-input__inner[readonly="readonly"] {
		border: 1px dashed #ababab;
		border-radius: 0px;
		padding: 0 12px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .el-input-number {
		text-align: left;
		width: 100%;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
		border: 1px dashed #ababab;
		border-radius: 0px;
		padding: 0 12px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .el-input-number /deep/ .is-disabled .el-input__inner {
		text-align: left;
		border: 1px dashed #ababab;
		border-radius: 0px;
		padding: 0 12px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	.add-update-preview .el-select {
		width: 100%;
	}
	.add-update-preview .el-select /deep/ .el-input__inner {
		border: 1px dashed #ababab;
		border-radius: 0px;
		padding: 0 12px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .el-select /deep/ .is-disabled .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 12px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .el-date-editor {
		width: 100%;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 30px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 30px;
		color: #000000;
		width: 100%;
		font-size: 16px;
		height: 34px;
	}
	.add-update-preview .viewBtn {
		border: 0px solid #ccc;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .viewBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .downBtn {
		border: 0px solid #ccc;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .downBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .unBtn {
		border: 0;
		cursor: not-allowed;
		border-radius: 4px;
		padding: 0 0px;
		margin: 0 20px 0 0;
		outline: none;
		color: #999;
		background: none;
		width: auto;
		font-size: 16px;
		line-height: 40px;
		height: 40px;
		.iconfont {
			margin: 0 2px;
			color: #fff;
			display: none;
			font-size: 14px;
			height: 34px;
		}
	}
	.add-update-preview .unBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
		border: 1px solid #ddd;
		cursor: pointer;
		border-radius: 0px;
		margin: 0 280px 0 0;
		color: #000000;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
		border: 1px solid #ddd;
		cursor: pointer;
		border-radius: 0px;
		margin: 0 280px 0 0;
		color: #000000;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
		border: 1px solid #ddd;
		cursor: pointer;
		border-radius: 0px;
		margin: 0 280px 0 0;
		color: #000000;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	.add-update-preview /deep/ .el-upload__tip {
		color: #666;
		font-size: 15px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 25px;
		color: #000000;
		width: 360px;
		font-size: 16px;
		line-height: 34px;
		height: 34px;
	}
	.add-update-preview .el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
				border: 1px solid #E8E8E8;
				border-radius: 0px;
				padding: 0 25px;
				color: #000000;
				width: 360px;
				font-size: 16px;
				line-height: 34px;
				height: 34px;
			}
	.add-update-preview .el-form-item.btn {
		padding: 0;
		margin: 20px 0 0;
		.btn1 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #6DB344;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn1:hover {
			opacity: 0.8;
		}
		.btn2 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #37A3D1;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 34px;
			}
		}
		.btn2:hover {
			opacity: 0.8;
		}
		.btn3 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #F5C5A9;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn3:hover {
			opacity: 0.8;
		}
		.btn4 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #ADADAC;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn4:hover {
			opacity: 0.8;
		}
		.btn5 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #FFBB33;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn5:hover {
			opacity: 0.8;
		}
	}
</style>
