<template>
	<div>
		<div class="login-container">
			<el-form class="login_form animate__animated animate__backInDown">
				<div class="login_form2">
					<div class="title-container">基于大数据的城市共享单车出行需求预测与行为分析</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							<span class="icon iconfont icon-touxiang04"></span>
						</div>
						<input placeholder="请输入账号：" name="username" type="text" v-model="rulesForm.username">
					</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							<span class="icon iconfont icon-touxiang05"></span>
						</div>
						<div class="password-box">
							<input placeholder="请输入密码：" name="password" :type="showPassword?'text':'password'" v-model="rulesForm.password">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item " v-if="roles.length>1">
						<div class="lable">
							<span class="icon iconfont icon-touxiang15"></span>
						</div>
						<div prop="loginInRole" class="list-type">
							<el-radio v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" v-bind:key="item.roleName" v-model="rulesForm.role" :label="item.roleName">{{item.roleName}}</el-radio>
						</div>
					</div>

		
					<div class="login-btn">
						<div class="login-btn1">
							<el-button v-if="loginType==1" type="primary" @click="login()" class="loginInBt">登录</el-button>
						</div>
						<div class="login-btn2">
							<el-button type="primary" @click="register('yonghu')" class="register">
								注册用户							</el-button>
						</div>
						<div class="login-btn3">
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>
<script>
	import 'animate.css'
	import menu from "@/utils/menu";
	export default {
		data() {
			return {
				verifyCheck2: false,
				flag: false,
				baseUrl:this.$base.url,
				loginType: 1,
				rulesForm: {
					username: "",
					password: "",
					role: "",
				},
				menus: [],
				roles: [],
				tableName: "",
				showPassword: false,
			};
		},
		mounted() {
			let menus = menu.list();
			this.menus = menus;

			for (let i = 0; i < this.menus.length; i++) {
				if (this.menus[i].hasBackLogin=='是') {
					this.roles.push(this.menus[i])
				}
			}

		},
		created() {

		},
		destroyed() {
		},
		components: {
		},
		methods: {

			//注册
			register(tableName){
				this.$storage.set("loginTable", tableName);
				this.$router.push({path:'/register',query:{pageFlag:'register'}})
			},
			// 登陆
			login() {

				if (!this.rulesForm.username) {
					this.$message.error("请输入用户名");
					return;
				}
				if (!this.rulesForm.password) {
					this.$message.error("请输入密码");
					return;
				}
				if(this.roles.length>1) {
					if (!this.rulesForm.role) {
						this.$message.error("请选择角色");
						return;
					}

					let menus = this.menus;
					for (let i = 0; i < menus.length; i++) {
						if (menus[i].roleName == this.rulesForm.role) {
							this.tableName = menus[i].tableName;
						}
					}
				} else {
					this.tableName = this.roles[0].tableName;
					this.rulesForm.role = this.roles[0].roleName;
				}
		
				this.loginPost()
			},
			loginPost() {
				this.$http({
					url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
					method: "post"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.$storage.set("Token", data.token);
						this.$storage.set("role", this.rulesForm.role);
						this.$storage.set("sessionTable", this.tableName);
						this.$storage.set("adminName", this.rulesForm.username);
						this.$nextTick(()=>{
							this.$http({
								url: this.tableName + '/session',
								method: "get"
							}).then(({
								data
							}) => {
								if (data && data.code === 0) {
									if(this.tableName == 'yonghu') {
										this.$storage.set('headportrait',data.data.touxiang)
									}
									if(this.tableName == 'users') {
										this.$storage.set('headportrait',data.data.image)
									}
									this.$storage.set('userForm',JSON.stringify(data.data))
									this.$storage.set('userid',data.data.id);
								} else {
									let message = this.$message
									message.error(data.msg);
								}
								if(this.boardAuth('hasBoard','查看',this.rulesForm.role)) {
									this.$router.replace({ path: "/board" });
								}else {
									this.$router.replace({ path: "/" });
								}
							});
						})
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
.login-container {
	min-height: 100vh;
	position: relative;
	background-repeat: no-repeat;
	background-position: center center;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20240910/60e1105deb3a4170b52246ca74ed3400.gif);
	background-repeat: no-repeat;
	background-size: cover !important;
	background: url(http://codegen.caihongy.cn/20240910/60e1105deb3a4170b52246ca74ed3400.gif);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;

	.login_form {
		padding: 30px 60px 10px 60px;
		margin: 0 auto;
		z-index: 1000;
		display: flex;
		flex-wrap: wrap;
		border-radius: 30px;
		box-shadow: 0px 4px 60px 0px #BFD1D1;
		flex-direction: column;
		background: #fff;
		width: 689px;
		align-items: flex-start;
		position: relative;
		height: auto;
		.login_form2 {
			width: 100%;
		}
		.title-container {
			padding: 0 40px;
			margin: 0 0 20px 0;
			color: #6CB342;
			background: none;
			font-weight: 500;
			width: 100%;
			font-size: 22px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			padding: 0;
			margin: 10px 0;
			display: flex;
			width: 100%;
			position: relative;
			height: 60px;
			.lable {
				color: #000;
				font-size: 16px;
				line-height: 40px;
				min-width: 0;
				text-align: left;
				.icon {
					border-radius: 100%;
					z-index: 1;
					color: #fff;
					top: 17%;
					left: 10px;
					background: #36A3D1;
					width: 40px;
					font-size: 14px;
					right: left;
					position: absolute;
					text-align: center;
					height: 40px;
				}
			}
			input {
				border: 1px solid #efeff7;
				border-radius: 30px;
				padding: 0 60px;
				box-shadow: 0px 4px 10px 0px rgba(191,209,209,0.3);
				color: #666;
				flex: 1;
				font-size: 16px;
				height: 60px;
			}
			input:focus {
				border: 1px solid #efeff7;
				border-radius: 30px;
				padding: 0 60px;
				box-shadow: 0px 4px 10px 0px rgba(191,209,209,0.3);
				outline: none;
				color: #666;
				flex: 1;
				font-size: 16px;
				height: 60px;
			}
			.password-box {
				display: flex;
				width: 100%;
				position: relative;
				align-items: center;
				input {
					border: 1px solid #efeff7;
					border-radius: 30px;
					padding: 0 60px;
					box-shadow: 0px 4px 10px 0px rgba(191,209,209,0.3);
					color: #666;
					flex: 1;
					font-size: 16px;
					height: 60px;
				}
				input:focus {
					border: 1px solid #efeff7;
					border-radius: 30px;
					padding: 0 60px;
					box-shadow: 0px 4px 10px 0px rgba(191,209,209,0.3);
					outline: none;
					color: #666;
					flex: 1;
					font-size: 16px;
					height: 60px;
				}
				.iconfont {
					cursor: pointer;
					z-index: 1;
					color: #000;
					top: 0;
					font-size: 16px;
					line-height: 60px;
					position: absolute;
					right: 20px;
				}
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
		}
		.list-type {
			border: 1px solid #efeff7;
			border-radius: 30px;
			padding: 0 30px 0 60px;
			box-shadow: 0px 4px 10px 0px rgba(191,209,209,0.3);
			color: #666;
			flex: 1;
			display: flex;
			width: 100%;
			font-size: 16px;
			align-items: center;
			flex-wrap: wrap;
			height: auto;
			/deep/ .el-radio__input .el-radio__inner {
				margin: 5px 0;
				background: rgba(53, 53, 53, 0);
				border-color: #666;
			}
			/deep/ .el-radio__input.is-checked .el-radio__inner {
				background: #6db344;
				border-color: #6db344;
			}
			/deep/ .el-radio__label {
				margin: 5px 0;
				color: #666;
				font-size: 16px;
			}
			/deep/ .el-radio__input.is-checked+.el-radio__label {
				color: #6db344;
				font-size: 16px;
			}
		}
		.login-btn {
			margin: 20px auto;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			.login-btn1 {
				width: 100%;
			}
			.login-btn2 {
				margin: 20px auto;
				display: flex;
				width: 100%;
				align-items: center;
				flex-wrap: wrap;
			}
			.login-btn3 {
				width: 100%;
			}
			.loginInBt {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				padding: 0 10px;
				margin: 0 0 10px;
				color: #fff;
				font-weight: 600;
				letter-spacing: 1px;
				font-size: 28px;
				border-radius: 60px;
				background: #6DB344;
				width: 100%;
				min-width: 68px;
				height: 60px;
			}
			.loginInBt:hover {
				opacity: 0.8;
			}
			.register {
				border: 2px solid #B8B8B8;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 20px;
				color: #B8B8B8;
				background: #fff;
				font-weight: 400;
				width: auto;
				font-size: 16px;
				height: 40px;
			}
			.register:hover {
				opacity: 0.8;
			}
			.forget {
				border: 0;
				cursor: pointer;
				border-radius: 0;
				padding: 0;
				margin: 0 10px 10px 0;
				color: #666;
				background: none;
				font-weight: 400;
				width: 100%;
				font-size: 16px;
				text-align: center;
				height: 34px;
			}
			.forget:hover {
				color: #0d6efd;
				opacity: 1;
			}
		}
	}
}

</style>
