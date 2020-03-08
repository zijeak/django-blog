window.onload = function(){
	// 给微信按钮绑定事件
	var wx = document.getElementsByClassName('wx')[0];
	var wx_code = document.getElementsByClassName('wx-code')[0];
	wx.onmouseover = function(){
		wx_code.style.display = 'block';
	};
	wx.onmouseout = function(){
		wx_code.style.display = 'none';
	};
}