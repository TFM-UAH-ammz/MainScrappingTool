var timout_id;
// NAVIGATION
function nav_games() {
	document.getElementById("global_search").style.display = "none";
	document.getElementById("global_site").style.display = 'block';
	if (document.getElementById("nav_u_drop").className == "nav_down back_form"){
        document.getElementById("nav_u_drop").className = "nav_up back_form";
	} else {
		document.getElementById("nav_u_drop").className = "nav_down back_form";
	}
	if (document.getElementById("nav_profile_load").className!=="content_25 nav_null"){
		document.getElementById("nav_profile_load").className="content_25 nav_null";
		multi_load('nav_profile','nav_profile_load','','');
		multi_load('nav_playthroughs','nav_playthroughs_load','','');
		multi_load('nav_games','nav_games_load','','');
	}
}

//Global
function limitText(limitField, limitCount, limitNum) {
    if (limitField.value.length > limitNum) {
        limitField.value = limitField.value.substring(0, limitNum);
    } else {
        limitCount.value = limitNum - limitField.value.length;
    }
}

function showNotification(page, option, param, param2, param3, param4, param5) {
	if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
		noti_xmlhttp = new XMLHttpRequest();
	} else {// code for IE6, IE5
		noti_xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	noti_xmlhttp.onreadystatechange=function(){
		if (noti_xmlhttp.readyState === 4 && noti_xmlhttp.status === 200 && option!=="toggleplaying" && option!=="delgame" && page!=="game") {
			document.getElementById("note_bar").innerHTML=noti_xmlhttp.responseText;
			document.getElementById("note_bar").style.display = 'block';
			setTimeout(function(){document.getElementById('note_bar').style.display = 'none';},6000);
		}
	};
	
	var sendinfo = "param="+encodeURIComponent(param)+"&param2="+encodeURIComponent(param2)+"&param3="+encodeURIComponent(param3)+"&param4="+encodeURIComponent(param4)+"&param5="+encodeURIComponent(param5);
	noti_xmlhttp.open("POST","funct/notifications?page="+page+"&option="+option,true);
	noti_xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	noti_xmlhttp.send(sendinfo);
}

//----------ORDER FLIP FOR USER AND SEARCH
function search_flip(flip, page){
	if (page=="search"){
		if (flip=="Normal Order"){
			flip="Reverse Order";
		} else {
			flip="Normal Order";	
		}
		document.forms.global_search_form.sortd.value=flip;
	}
	if (page=="user"){
		if (flip=="Normal"){
			flip="Reverse";
		} else {
			flip="Normal";	
		}
		document.forms.usergames.sortd.value=flip;
	}
}

function multi_load(page, id, option, option_b) {
  var xhttp;
  if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
		xhttp = new XMLHttpRequest();
	} else {// code for IE6, IE5
		xhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState===4 && xhttp.status===200) {
			multi_loaded(id, this);
		}
  };
  var params = "option="+encodeURIComponent(option)+"&option_b="+encodeURIComponent(option_b);
	xhttp.open("POST",page,true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(params);
}

function multi_loaded(id, xhttp) {
  document.getElementById(id).innerHTML=xhttp.responseText;
}

function change_class(element, class_name){
	document.getElementById(element).className=class_name;
}

// GLOBAL SEARCH
function initialize() {
	var hash = location.hash;
	if (hash.substring(0, 7) === "#search"){
		//Get Page
		hash = location.hash.substr(7);
		if (hash > 0){
			if (isNaN(hash) === false){} 
			else {hash = 1}
		} else {
			hash = 1
		}
		globalSearch(document.forms.global_search_form.t.value,hash,document.forms.global_search_form.q.value);
	} else {
		document.getElementById("global_search").style.display = "none";
		document.getElementById("global_site").style.display = 'block';
	}
}

function search_enable(opt){
	document.getElementById("nav_u_drop").className = "nav_up back_form";
	if (document.getElementById("global_search").style.display === "none"){
		document.getElementById("global_site").style.display = 'none';
		document.getElementById("global_search").style.display = "block";
		document.getElementById("global_search_box").focus();
		if (document.getElementById("global_search_box").className!=="global_search_box back_form nav_null"){
			document.getElementById("global_search_box").className="global_search_box back_form nav_null";
			//If Page Set
			var hash = location.hash;
			if (hash.substring(0, 7) === "#search"){
				//Get Page
				hash = location.hash.substr(7);
				if (hash > 1){
					if (isNaN(hash) === false){} 
					else {hash = 1}
				}
			} else {
				hash = 1;
			}
			globalSearch(document.forms.global_search_form.t.value,hash,document.forms.global_search_form.q.value);
		}
	} else if (opt === "close") {
		document.getElementById("global_search").style.display = "none";
		document.getElementById("global_site").style.display = 'block';
	}
}

function search_options() {
	if (document.getElementById("global_search_opt").style.display === 'block'){
		document.getElementById("global_search_opt").style.display = 'none';
	} else {
		document.getElementById("global_search_opt").style.display = 'block';
	}
}

function hitkey_l(key, type, inputString){
	if(key===9 || key===16 || key===17 || key===18 || key===20 || key===116) {
		return false;
	} else if(document.getElementById("global_search").style.display === "none" && (key>=33 && key<=40)){
		return false;
	} else if(key===27) {
		document.getElementById("global_search").style.display = "none";
		document.getElementById("global_site").style.display = 'block';
	} else {
		globalSearch(type,1,inputString, 750);
	}
}

function globalSearch(type, page, str, timeout) {
	if (typeof type === 'undefined' || !type) {type = "games";}
	if (typeof page === 'undefined' || !page) {page = 1;}
	if (typeof str === 'undefined' || !str) {str = document.forms.global_search_form.q.value;}
	if (typeof timeout === 'undefined' || !timeout) {timeout = 50;}
	if (timout_id) {
		clearTimeout(timout_id);
	}
	timout_id = setTimeout(function(){
		//ALL
		document.getElementById("global_site").style.display = 'none';
		document.getElementById("global_search").style.display = 'block';
		asc = document.forms.global_search_form.sortd.value;
		if (str.trim() === "" && page > 1){
			location.hash = "search"+page;
		} else {
			location.hash = "search"
		}
		if (type==="games"){
			document.getElementById("search_preset_u").style.display = 'none';
			document.getElementById("search_preset_g").style.display = 'block';
			document.getElementById("search_detail_box").style.display = 'block';
			option = document.forms.global_search_form.search_sort_g.value;
			platform = document.forms.global_search_form.platform.value;
			length_type = document.forms.global_search_form.search_range_type.value;
			length_min = document.forms.global_search_form.search_len_min_g.value.replace(/[^0-9.]/g, '');
			length_max = document.forms.global_search_form.search_len_max_g.value.replace(/[^0-9.]/g, '');
			document.forms.global_search_form.search_len_min_g.value = length_min;
			document.forms.global_search_form.search_len_max_g.value = length_max;
			detail = document.forms.global_search_form.detail.value;
		} else if (type==="users"){
			document.getElementById("search_preset_g").style.display = 'none';
			document.getElementById("search_preset_u").style.display = 'block';
			document.getElementById("search_detail_box").style.display = 'none';
			option = document.forms.global_search_form.search_sort_u.value;
			platform = "";
		}
		if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
			search_xmlhttp = new XMLHttpRequest();
		} else {// code for IE6, IE5
			search_xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		search_xmlhttp.onreadystatechange=function(){
			if (search_xmlhttp.readyState===4 && search_xmlhttp.status===200) {
				document.getElementById("global_search_content").innerHTML=search_xmlhttp.responseText;
				if (page > 1){
					setTimeout(function(){
						document.getElementById("global_search_content").scrollIntoView(true);
					}, 50);
				}
			} else {
				document.getElementById("global_search_content").innerHTML="<div class='global_padding center'><div class='loading_bar'></div></div>";
			}
		};
		var params = "queryString="+encodeURIComponent(str)+"&t="+type+"&sorthead="+option+"&sortd="+asc+"&plat="+encodeURIComponent(platform)+"&length_type="+length_type+"&length_min="+length_min+"&length_max="+length_max+"&detail="+detail;
		search_xmlhttp.open("POST","search_results?page="+page,true);
		search_xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		search_xmlhttp.send(params);
		//if (document.forms.global_search_form.q.value !== str) {document.forms.global_search_form.q.value = str;}
	}, timeout);
}

// game.php


// user.php
function userStats(user, cat, platform, year) {
		if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp = new XMLHttpRequest();
		} else {// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function(){
			if (xmlhttp.readyState===4 && xmlhttp.status===200) {
				document.getElementById("user_stats").innerHTML=xmlhttp.responseText;
			} else {
				document.getElementById("user_stats").innerHTML="<div class='global_padding center'><div class='loading_bar'></div></div>";
			}
		};
		var params = "n="+encodeURIComponent(user)+"&c="+encodeURIComponent(cat)+"&p="+encodeURIComponent(platform)+"&y="+encodeURIComponent(year);
		xmlhttp.open("POST","user_stats_more",true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xmlhttp.send(params);
}

function hitkey_ul(key, inputString, username){
	if(key==9 || key==13 || key==16 || key==17 || key==18 || key==20) {
		return false;
	} else {
		userGames(inputString,username,document.forms.usergames.platform.value,document.forms.usergames.sortby.value, document.forms.usergames.sortd.value, 750);
	}
}

function userCollection(str, user, platform, option, asc, timeout) {
	if (typeof timeout === 'undefined' || !timeout) {timeout = 50;}
	if (timout_id) {
		clearTimeout(timout_id);
	}
	timout_id = setTimeout(function(){
		if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp = new XMLHttpRequest();
		} else {// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function(){
			if (xmlhttp.readyState===4 && xmlhttp.status===200) {
				document.getElementById("user_collection").innerHTML=xmlhttp.responseText;
			} else {
				document.getElementById("user_collection").innerHTML="<div class='loading_bar'></div>";
			}
		};
		var params = "queryString="+encodeURIComponent(str)+"&n="+user+"&p="+platform+"&sortd="+asc+"&h="+option;
		xmlhttp.open("POST","user_collection_list",true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xmlhttp.send(params);
	}, timeout);
}

function userGames(str, user, platform, option, asc, timeout) {
	if (typeof timeout === 'undefined' || !timeout) {timeout = 50;}
	if (timout_id) {
		clearTimeout(timout_id);
	}
	timout_id = setTimeout(function(){
		if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp = new XMLHttpRequest();
		} else {// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function(){
			if (xmlhttp.readyState===4 && xmlhttp.status===200) {
				document.getElementById("user_games").innerHTML=xmlhttp.responseText;
			} else {
				document.getElementById("user_games").innerHTML="<div class='loading_bar'></div>";
			}
		};
		var  view, playing, backlog, replays, custom, custom2, custom3, completed, retired;
		view = document.forms.usergames.view.value;
		if (document.forms.usergames.list_p.value==1){playing = 1;}
		if (document.forms.usergames.list_b.value==1){backlog = 1;}
		if (document.forms.usergames.list_r.value==1){replays = 1;}
		if (document.forms.usergames.list_c.value==1){custom = 1;}
		if (document.forms.usergames.list_c2.value==1){custom2 = 1;}
		if (document.forms.usergames.list_c3.value==1){custom3 = 1;}
		if (document.forms.usergames.list_cp.value==1){completed = 1;}
		if (document.forms.usergames.list_rt.value==1){retired = 1;}
		var params = "queryString="+encodeURIComponent(str)+"&n="+user+"&v="+view+"&playing="+playing+"&backlog="+backlog+"&replays="+replays+"&custom="+custom+"&custom2="+custom2+"&custom3="+custom3+"&completed="+completed+"&retired="+retired+"&p="+encodeURIComponent(platform)+"&sortd="+asc+"&h="+option;
		xmlhttp.open("POST","user_games_list",true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xmlhttp.send(params);
		if (document.forms.usergames.showname.value !== str) {document.forms.usergames.showname.value = str;}
	}, timeout);
}

function userGamesToggle(usr, cat, color){
	var type = [["list_p",document.getElementById("list_p_value").value],["list_b",document.getElementById("list_b_value").value],["list_r",document.getElementById("list_r_value").value],
    				["list_c",document.getElementById("list_c_value").value],["list_c2",document.getElementById("list_c2_value").value],["list_c3",document.getElementById("list_c3_value").value],
    				["list_cp",document.getElementById("list_cp_value").value],["list_rt",document.getElementById("list_rt_value").value]];
	for (var value_set in type) {
		if (type[value_set][0]==cat){
			if (document.getElementById(type[value_set][0]+"_value").value==0){
				document.getElementById(type[value_set][0]+"_value").value=1;
				document.getElementById(type[value_set][0]).className="user_games_nav "+color;
			} else if (document.forms.usergames.list_multi.value>=2){
				document.getElementById(type[value_set][0]+"_value").value=0;
				document.getElementById(type[value_set][0]).className="user_games_nav back_dark";
			}
		} else {
			if (document.forms.usergames.list_multi.value<=1){
				document.getElementById(type[value_set][0]+"_value").value=0;
				document.getElementById(type[value_set][0]).className="user_games_nav back_dark";
			}
		}
	}
	var timeout;
	if (document.forms.usergames.list_multi.value>=2){timeout = 1000;}
	else {timeout = 50;}
	if (timout_id) {clearTimeout(timout_id);}
	timout_id = setTimeout(function(){
		userGames(document.forms.usergames.showname.value,usr,document.forms.usergames.platform.value,document.forms.usergames.sortby.value,document.forms.usergames.sortd.value);
	}, timeout);
}

function userGamesDetail(playId, playStyle, selector) {
	if (document.getElementById(selector+playId).style.display === "none"){
		document.getElementById(selector+playId).style.display = "table-cell";
		if (document.getElementById(selector+playId).className!=="user_null"){
			document.getElementById(selector+playId).className="user_null";
			document.getElementById(selector+playId).innerHTML="<div class='loading_bar'></div>";
			multi_load("user_games_detail",selector+playId,playId,playStyle);
		}
	} else {
		document.getElementById(selector+playId).style.display = "none";	
	}
}

function setNowPlaying(playId, original, selector) {
	showNotification("user","toggleplaying",playId,null,null,null,null);
    if (document.getElementById(selector+playId).className !== "text_green") {
    	document.getElementById(selector+playId).className = "text_green";
    } else {
    	document.getElementById(selector+playId).className = original;
    }
}

function confirmDelete(delId, gameName, selector) {
    msgQuestion = "Are you sure you want to delete "+gameName+"?";
    userResponse = confirm(msgQuestion);
    if (userResponse == 1) {
    	showNotification("user","delgame",delId,null,null,null,null);
    	document.getElementById(selector+delId).style.display = "none";
    } else {
        return;
    }
}

//forum.php
function editComment($option) { //WYSIWYG
	if ($option.toLowerCase() == "url"){var $usrinput=prompt("Please enter the URL","http://");}
	if ($option.toLowerCase() == "youtube"){var $usrinput=prompt("Please enter full YouTube URL","http://");}
	if ($option.toLowerCase() == "img"){var $usrinput=prompt("Please enter the image URL","http://");}
	if (!$usrinput){var $usrinput="";}
	
    var textarea = document.forms.create_post.post_comment;
    if ('selectionStart' in textarea) {
            // check whether some text is selected in the textarea
        if (textarea.selectionStart != textarea.selectionEnd && ($option.toLowerCase()!="youtube" && $option.toLowerCase()!="img")) {
        	if ($option.toLowerCase() == "url"){$usrinput = "="+$usrinput;}
            var newText = textarea.value.substring (0, textarea.selectionStart) + 
                "["+$option+$usrinput+"]" + textarea.value.substring  (textarea.selectionStart, textarea.selectionEnd) + "[/"+$option+"]" +
                textarea.value.substring (textarea.selectionEnd);
            textarea.value = newText;
        } else {
        	var newText = textarea.value.substring (0, textarea.selectionStart) + 
                "["+$option+"]"+$usrinput+"[/"+$option+"]" +
                textarea.value.substring (textarea.selectionEnd);
            textarea.value = newText;
        }
    } else {  // Internet Explorer before version 9
            // create a range from the current selection
        var textRange = document.selection.createRange ();
            // check whether the selection is within the textarea
        var rangeParent = textRange.parentElement ();
        if (rangeParent === textarea && ($option.toLowerCase()!="youtube" && $option.toLowerCase()!="img")) {
        	if ($option.toLowerCase() == "url"){$usrinput = "="+$usrinput;}
            textRange.text = "["+$option+$usrinput+"]" + textRange.text + "[/"+$option+"]";
        } else {
        	textRange.text = "["+$option+"]"+$usrinput+"[/"+$option+"]";
        }
    }
}

// submit.php
function hitkey_s(key, inputString, page){
	if(key==9 || key==13 || key==16 || key==17 || key==18 || key==20) {
		return false;
	} else {
		submitList(inputString, page, 750);
	}
}

function submitList(str, page, timeout) {
	if ((typeof str === 'undefined' || !str) && page == "forum_main") {str = document.forms.create_post.game_name.value;}
	if ((typeof str === 'undefined' || !str) && page == "submit") {str = document.forms.submit_game.game_name.value;}
	if (typeof timeout === 'undefined' || !timeout) {timeout = 50;}
	if (timout_id) {
		clearTimeout(timout_id);
	}
	timout_id = setTimeout(function(){
		if (str.length > 0) {
			if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
				xmlhttp = new XMLHttpRequest();
			} else {// code for IE6, IE5
				xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
			xmlhttp.onreadystatechange=function(){
				if (xmlhttp.readyState===4 && xmlhttp.status===200) {
					document.getElementById("submit_gamelist").innerHTML=xmlhttp.responseText;
				} else {
					document.getElementById("submit_gamelist").innerHTML="<div class='loading_bar'></div>";
				}
			};
			var params = "queryString="+encodeURIComponent(str);
			xmlhttp.open("POST","submit_list?page="+page,true);
			xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
			xmlhttp.send(params);
		} else if (page == "forum_main") {
			document.forms.create_post.game_id.value='0';
			document.getElementById('game_title_set').innerHTML='Not Set';
			document.getElementById('game_title_set').className='text_red';
			document.getElementById('submit_gamelist').innerHTML='';
		}
	}, timeout);
}