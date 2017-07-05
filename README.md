colorToVal
-------------
一个输入颜色的16进制可转为对应变量的Sublime Text 3自动完成插件。

#####插件效果：（colorToVal）
![效果演示图](colorToVal.gif)

<!-- #### 安装(Package Control)
* Ctrl+Shift+P 输入 Package Control: Install Packag
* 搜索 colorToVal
* 重启 Sublime Text -->

#### 安装(github)
* Ctrl+Shift+P 输入 Package Control: Add Repository
* 添加git地址 https://github.com/yh418807968/colorToVal
* Ctrl+Shift+P 输入 Package Control: Install Package
* 搜索 colorToVal
* 重启 Sublime Text

##### 配置参数

参数配置默认文件：Sublime Text -> Preferences -> Package Settings -> colorToVal -> setting-Default

* `exts` - 启用此插件的文件类型。默认为：[".css", ".scss", ".less", ".sass", ".styl"]。
* `data` - 用户自定义的数据。默认举例为：
	"data":{
    
			"$c-bg1":"#dadada",
			"$c-night":"#000",
			"$c-bg2-night":"#000",
			"$c-bg3":"#fff",    
	}。
	用户在setting-User中设置数据后，将覆盖此数据。
	
用户参数配置文件：Sublime Text -> Preferences -> Package Settings -> colorToVal -> setting-User
	{
		"data":{
			//your data here   
		}
	}
	注：key变量名为，value为16进制色值，一个16进制色值可对应多个变量。

##### 使用
输入16进制色值(可省略#)，以字母t为触发快捷键，找到对应的变量，按enter键替换。详情见动图colorToVal.gif


@ youhong SOHU SNS FE-Group
