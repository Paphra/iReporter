

window.onload = function () {
    // check to see whether there are some cookies for this user

    // see if the user is already logged in
}


function checkCookies() {
    // code for checking cookies to see if the user already signed in
}

function signup() {

    var date = new Date();
    var day = date.getDay();
    var month = date.getMonth();
    var year = date.getFullYear();
    var h = date.getHours();
    var m = date.getMinutes();
    var s = date.getSeconds();

    var cDate = year + " - " + month + " - " + day + " " + h + ":" + m + ":" + s;
    var u_id = parseInt((Math.floor(Math.random() * 10) + 1) + "" + (Math.floor(Math.random() * 10) + 1)
        + "" + (Math.floor(Math.random() * 10) + 1) + "" + (Math.floor(Math.random() * 10) + 1)
        + "" + (Math.floor(Math.random() * 10) + 1) + "" + (Math.floor(Math.random() * 10) + 1)
        + "" + (Math.floor(Math.random() * 10) + 1) + "" + (Math.floor(Math.random() * 10) + 1)
        + "" + (Math.floor(Math.random() * 10) + 1) + "" + (Math.floor(Math.random() * 10) + 1));

    var fname = document.forms["form-signup"]["firstName"].value;
    var lname = document.forms["form-signup"]["lastName"].value;
    var occupation = document.forms["form-signup"]["occupation"].value;
    var address = document.forms["form-signup"]["address"].value;
    var sex = document.forms["form-signup"]["gender"].value;
    var email = document.forms["form-signup"]["email"].value;
    var phoneNumber = document.forms["form-signup"]["phoneNumber"].value;
    var uname = document.forms["form-signup"]["username"].value;
    var pass = document.forms["form-signup"]["password"].value;
    var passC = document.forms["form-signup"]["confirmPassword"].value;
    if (pass == passC) {
        // signup logic here

        return true

    } else {
        document.forms["form-signup"]["password"].requestFocus;
        return false;
    }
}

function checkUname(value) {
    // code for username validation
    var unameErr = document.getElementById("usernameErr");

}

function checkPassword() {
    var pass = document.forms["form-signup"]["password"].value;
    var passC = document.forms["form-signup"]["confirmPassword"].value;
    var btnSubmit = document.forms['form-signup']['submit'];
    var pwdErr = document.getElementById("passwordError");
    if (passC != pass) {
        pwdErr.innerHTML = "<p style='color:red;'>Password Mismatch!</p>";
        btnSubmit.disable = true;
    } else if (passC == '' || pass == '') {
        pwdErr.innerHTML = '';
        btnSubmit.disable = true;
    } else {
        pwdErr.innerHTML = "<p style='color:green;'>Password Match!</p>";
        btnSubmit.disable = false;
    }
}


function signin() {

    var uname = document.forms["form-signin"]["login-name"].value;
    var pass = document.forms["form-signin"]["password"].value;
    var signErr = document.getElementById("signinError");
    var passC = "0"
    var unameC = "0"
    if (pass == passC && uname == unameC) {
        // signin logic here

        return true

    } else {
        signErr.innerHTML = "<p style='color:red;>Username or Password Incorrect!</p>";
        return false;
    }
}

function loadProfile() {
    // code for loading the profile is here
    var username = "";

    // code for fetching the data

    // load the page
    var u_id = "paphra";

    var u_info_p = document.getElementById("user-info");
    var u_info = "<div class='userInfo'>" +
        "Full Name : as Username : email-address : Phone Number : Address </div>";
    u_info_p.innerHTML = u_info;

    loadResolved("fi-resolved-user", u_id);
    loadInv("fi-inv-user", u_id);
    loadRejected("fi-rejected-user", u_id);
    loadAll("all-fi-list-user", u_id);

}

function loadAllUserReports() {
    var u_id = "pa";

    loadAll("all-fi-list-user", u_id);

}

function loadResolved(p_id, user_id) {
    var total = 4;
    var flags = 2;
    var html = "";
    var fi_id = "";
    for (var i = 1; i < (total + 1); i++) {
        if (i < flags + 1) {
            html += "<li class='flag'>" +
                "<h3><img src='assets/img/flag-icon.png' width='3%' />Title [Red Flag]</h3>" +
                "<p><b>Short Descrption</b> ...Date: 2018 / 11 / 23</p>" +
                "<P>Location [lat and long]</a></p>" +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>" +
                "</li>";
        } else {
            html += "<li class='inter'>" +
                "<h3><img src='assets/img/inter-icon.png' width='3%'' />Title [Intervention]</h3>" +
                "<p><b>Short Descrption</b> ... Date: 2018/11/23</p>" +
                "<P>Location [lat and long]</p>" +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>" +
                "</li>";
        }
    }

    document.getElementById(p_id).innerHTML = html;


}

function loadInv(p_id, user_id) {
    var total = 3
    var flags = 1;
    var html = "";
    var fi_id = "";
    for (var i = 1; i < (total + 1); i++) {
        if (i < flags + 1) {
            html += "<li class='flag'>" +
                "<h3><img src='assets/img/flag-icon.png' width='3%' />Title [Red Flag]</h3>" +
                "<p><b>Short Descrption</b> ...Date: 2018 / 11 / 23</p>" +
                "<P>Location [lat and long]</p>" +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>" +
                "</li>";
        } else {
            html += "<li class='inter'>" +
                "<h3><img src='assets/img/inter-icon.png' width='3%'' />Title [Intervention]</h3>" +
                "<p><b>Short Descrption</b> ... Date: 2018/11/23</p>" +
                "<P>Location [lat and long]</p>" +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>" +
                "</li>";
        }
    }

    document.getElementById(p_id).innerHTML = html;
}

function loadRejected(p_id, user_id) {
    var total = 5;
    var flags = 2;
    var html = "";
    var fi_id = "";
    for (var i = 1; i < total + 1; i++) {
        if (i < flags + 1) {
            html += "<li class='flag'>" +
                "<h3><img src='assets/img/flag-icon.png' width='3%' />Title [Red Flag]</h3>" +
                "<p><b>Short Descrption</b> ...Date: 2018 / 11 / 23</p>" +
                "<P>Location [lat and long]</p>" +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>" +
                "</li>";
        } else {
            html += "<li class='inter'>" +
                "<h3><img src='assets/img/inter-icon.png' width='3%'' />Title [Intervention]</h3>" +
                "<p><b>Short Descrption</b> ... Date: 2018/11/23</p>" +
                "<P>Location [lat and long]</p>" +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>" +
                "</li>";
        }

    }

    document.getElementById(p_id).innerHTML = html;
}
function loadAll(p_id, user_id) {

    var list = ["flag", "inter", "flag-inv", "inter-inv", "flag"];

    var all = "";
    var fi_id = "";

    for (var i = 0; i < (list.length); i++) {

        if (list[i] === "flag") {
            all += "<li class='flag'>" +
                "<h3><img src='assets/img/inter-icon.png' width='3%'' />Title [Red Flag]</h3>" +
                ": <b>Short Descrption</b> ... Date: 2018/11/23 " +
                ": <b>Status</b> " +
                ": Location [lat and long] " +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>";
            if (user_id != "admin") {
                all += "<button onclick='showEdit(\"" + fi_id + "\",\"" + user_id + "\")'>Edit</button>" +
                    "<button onclick='showDelete(\"" + fi_id + "\",\"" + user_id + "\")'>Delete</button>";
            }
            all += "<br/>" +
                "<div id='jsDisplay'><div>" +
                "</li>";

        } else if (list[i] === "inter") {
            all += "<li class='inter'>" +
                "<h3><img src='assets/img/inter-icon.png' width='3%'' />Title [Intervention]</h3>" +
                ": <b>Short Descrption</b> ... Date: 2018/11/23 " +
                ": <b>Status</b> " +
                ": Location [lat and long] " +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>";
            if (user_id != "admin") {
                all += "<button onclick='showEdit(\"" + fi_id + "\",\"" + user_id + "\")'>Edit</button>" +
                    "<button onclick='showDelete(\"" + fi_id + "\",\"" + user_id + "\")'>Delete</button>";
            }
            all += "<br/>" +
                "<div id='jsDisplay'><div>" +
                "</li>";
        } else if (list[i] === "flag-inv") {
            all += "<li class='flag-inv'>" +
                "<h3><img src='assets/img/inter-icon.png' width='3%'' />Title [Red Flag]</h3>" +
                ": <b>Short Descrption</b> ... Date: 2018/11/23 " +
                ": <b>Under Investigation</b> " +
                ": Location [lat and long] " +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>";
            if (user_id != "admin") {
                //all += "<button onclick='showEdit(\"fi_id\")'>Edit</button>" +
                //"<button onclick='showDelete(\"fi_id\")'>Delete</button>";
            }
            all += "<br/>" +
                "<div id='jsDisplay'><div>" +
                "</li>";
        } else {
            all += "<li class='inter-inv'>" +
                "<h3><img src='assets/img/inter-icon.png' width='3%'' />Title [Intervention]</h3>" +
                ": <b>Short Descrption</b> ... Date: 2018/11/23 " +
                ": <b>Under Investigations</b> " +
                ": Location [lat and long] " +
                "<button onclick='showDetails(\"" + fi_id + "\",\"" + user_id + "\")'>Details</button>";
            if (user_id != "admin") {
                //all += "<button onclick='showEdit(\"fi_id\")'>Edit</button>" +
                //"<button onclick='showDelete(\"fi_id\")'>Delete</button>";
            }
            all += "<br/>" +
                "<div id='jsDisplay'><div>" +
                "</li>";
        }

    }

    document.getElementById(p_id).innerHTML = all;

}

function loadAdmin() {

    var u_id = "admin";

    var a_info_p = document.getElementById("admin-info");
    var a_info = "<div class='userInfo'>" +
        "Full Name : as Username : email-address : Phone Number : Address </div>";
    a_info_p.innerHTML = a_info;

    loadResolved("fi-resolved-admin", u_id);
    loadInv("fi-inv-admin", u_id);
    loadRejected("fi-rejected-admin", u_id);
    loadAll("all-fi-list-admin", u_id);

}

function loadAdminAll() {

    // code for loading the admin page is here
    loadAll("all-fi-list-admin", "admin");
}

function loadIndividualReports() {
    // code for loading individual reports for each user goes here
}

function showDetails(fi_id, user_id) {
    // code goes here
    if (user_id == "admin") {
        window.location.href = "admin-details.html";

    } else {

        window.location.href = "user-details.html";
    }
}

function loadUserDetails(fi_id) {
    // code here
    var holder = document.getElementById("detail-fi");
    var table = "<form name='form-user-details' ><fieldset>" +
        "<table width='90%' align='center'>" +
        "<tr><td align='right' width='50%'>Type:</td><td align='left'>Red-Flag</td ></tr>" +
        "<tr><td align='right' width='50%'>Status:</td><td align='left'>Status [Draft, Under Investigation, Resolved, Rejectd]</td ></tr>" +
        "<tr><td align='right'>Subject:</td><td align='left'>Subject Matter</td></tr>" +
        "<tr><td align='right'>Comments:</td><td align='left'>The comments from the user who reported this red flag or intervention</td></tr>" +
        "<tr><td align='center' colspan='2'><hr />Geolocation<hr /></td></tr>" +
        "<tr><td align='right'>Latitude:</td><td align='left'>" +
        "<input type='number' name='latitude' disabled value='0.3476' /></td></tr>" +
        "<tr><td align='right'>Longitude:</td><td align='left'>" +
        "<input type='number' name='longitude' disabled value='32.5825' /></td></tr>" +
        "<tr><td align='center' colspan='2'><div id='map-sample'></div></td></tr>" +
        "<tr><td align='center' colspan='2'><hr />Evidence<hr /></td></tr>" +
        "<tr><td align='right'>Images:</td><td align='left'><img src='' width='100%' height='100px' /></td></tr>" +
        "<tr><td align='right'>Videos:</td><td align='left'><video src='' width='30%' height='100px' /></td></tr>" +
        "<tr><td align='right'>Others:</td><td align='left'><a href='file' >Download Files</a></td></tr>" +
        "</table ></fieldset></form><hr/>";

    holder.innerHTML = table;

}

function loadAdminDetails(fi_id) {
    // code here
    var holder = document.getElementById("detail-fi");
    var table = "<form name='form-admin-details' ><fieldset>" +
        "<table width='90%' align='center'>" +
        "<tr><td align='right' width='50%'>Type:</td><td align='left'>Red-Flag</td ></tr>" +
        "<tr><td align='right' width='50%'>By:</td><td align='left'>Full Name of The User</td ></tr>" +
        "<tr><td align='right' width='50%'>Status:</td><td align='left'>" +
        "<select name='status' onselect='saveChangeStatus(\"fi_id\")'><option value='draft'>Draft</option>" +
        "<option value='under-inv'>Under Investigation</option><option value='resolved'>Resolved</option>" +
        "<option value='rejected'>Rejected</option></select></td ></tr > " +
        "<tr><td align='right'>Subject:</td><td align='left'>Subject Matter</td></tr>" +
        "<tr><td align='right'>Comments:</td><td align='left'>The comments from the user who reported this red flag or intervention</td></tr>" +
        "<tr><td align='center' colspan='2'><hr />Geolocation<hr /></td></tr>" +
        "<tr><td align='right'>Latitude:</td><td align='left'>" +
        "<input type='number' name='latitude' disabled value='0.3476' /></td></tr>" +
        "<tr><td align='right'>Longitude:</td><td align='left'>" +
        "<input type='number' name='longitude' disabled value='32.5825' /></td></tr>" +
        "<tr><td align='center' colspan='2'><div id='map-sample'></div></td></tr>" +
        "<tr><td align='center' colspan='2'><hr />Evidence<hr /></td></tr>" +
        "<tr><td align='right'>Images:</td><td align='left'><img src='' width='100%' height='100px' /></td></tr>" +
        "<tr><td align='right'>Videos:</td><td align='left'><video src='' width='30%' height='100px' /></td></tr>" +
        "<tr><td align='right'>Others:</td><td align='left'><a href='file' >Download Files</a></td></tr>" +
        "</table ></fieldset></form><hr/>";

    holder.innerHTML = table;

}


function showEdit(fi_id) {
    // code goes here
    //window.location.href = "edit.html?" + fi_id;
    window.location.replace("edit.html");
    loadEdit(fi_id);
}

var c_id = "";

function loadEdit(fi_id) {
    var holder = document.getElementById("edit-fi");
    var form = "<form name='form-edit' action='' onsubmit='saveEdit(\"fi_id\")' >" +
        "<fieldset>" +
        "<table width='90%' align='center'>" +
        "<tr><td align='right' width='50%'>Type:</td><td align='left'>" +
        "<select name='type' size='1' class='s-type'><option value='flag'>Red-Flag</option>" +
        "<option value='intervention'>Intervention</option></select ></td ></tr>" +
        "<tr><td align='right'>Subject:</td><td align='left'>" +
        "<input type = 'text' name = 'title' placeholder = 'Subject matter' value='' required size='50' maxlength='70' /></td></tr>" +
        "<tr><td align='right'>Comments:</td><td align='left'>" +
        "<textarea name='comments' placeholder='Describe the Occurence' value='' required cols='50' rows='8'></textarea></td></tr>" +
        "<tr><td align='center' colspan='2'><hr />Geolocation<hr /></td></tr>" +
        "<tr><td align='right'>Latitude:</td><td align='left'>" +
        "<input type='number' name='latitude' required max='90' min='0' id='lat' oninput='cShowMap(\"edit\")' value='0.3476' /></td></tr>" +
        "<tr><td align='right'>Longitude:</td><td align='left'>" +
        "<input type='number' name='longitude' required max='180' min='0' id='long' oninput='cShowMap(\"edit\")' value='32.5825' /></td></tr>" +
        "<tr><td align='center' colspan='2'><div id='map-sample'></div></td></tr>" +
        "<tr><td align='center' colspan='2'><hr />Evidence<hr /></td></tr>" +
        "<tr><td align='right'>Images:</td><td align='left'>" +
        "<input type='file' name='image' value='' multiple accept='.jpeg, .png, .gif, .jpg'/></td></tr>" +
        "<tr><td align='right'>Videos:</td><td align='left'>" +
        "<input type='file' namae='video' value='' accept='.mp4, .ogg' multiple/></td></tr>" +
        "<tr><td align='right'>Others:</td><td align='left'>" +
        "<input type='file' name='other' multiple accept='.doc, .docx, .mp3, .wav, .xls, .xlsx, .ppt, .pptx' /></td></tr>" +
        "</table ><hr/>" +
        "<input type='submit' name='save' value='Save' class='btn-save' /></fieldset></form>";

    holder.innerHTML = form;

}

function cShowMap(name) {
    // code goes here
    var lat = document.forms["form-" + name]["latitude"].value;
    var lng = document.forms["form-" + name]["longitude"].value;

    if (long == '') {
        lng = 0
    } else if (lat == '') {
        lat = 0;
    } else {
        lat = parseFloat(lat);
        lng = parseFloat(lng);
    }

    var holder = document.getElementById("map-sample");

    showMap(lat, lng, holder);

}

function showMap(lat, lng, holder) {
    var my_p = new google.maps.LatLng(lat, lng);
    var opts = {
        zoom: 10,
        center: my_p,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(holder, opts);

    var marker = goole.maps.Marker({
        postion: my_p,
        map: map,
        title: "Current Position"
    });
}

function showDelete(fi_id) {
    // code goes here
    if (confirm("Are you sure you want to delete the this iReport with ID " + fi_id + "?")) {
        // delete the item

        alert("iReport [" + fi_id + "] Deleted!")
        window.location.reload(true);

    } else {
        // the user does not want to delete the flag or inter
    }
}

function loadImage() {
    // code here
}


function createReport() {

    var date = new Date();
    var day = date.getDay();
    var month = date.getMonth();
    var year = date.getFullYear();
    var h = date.getHours();
    var m = date.getMinutes();
    var s = date.getSeconds();

    var status = "Draft";

    var cDate = year + " - " + month + " - " + day + " " + h + ":" + m + ":" + s;

    var fi_id = parseInt((Math.floor(Math.random() * 10) + 1) + "" + (Math.floor(Math.random() * 10) + 1)
        + "" + (Math.floor(Math.random() * 10) + 1) + "" + (Math.floor(Math.random() * 10) + 1)
        + "" + (Math.floor(Math.random() * 10) + 1));

    var type = document.forms["form-create"]["type"].value;
    var subj = document.forms["form-create"]["title"].value;
    var desc = document.forms["form-create"]["comments"].value;
    var lat = document.forms["form-create"]["latitude"].value;
    var long = document.forms["form-create"]["longitude"].value;
    var imgs = document.forms["form-create"]["image"].value;
    var vids = document.forms["form-create"]["video"].value;
    var others = document.forms["form-create"]["other"].value;

    var location = lat + ";" + long;

    // then upload the data. Sve it code here
}

function saveEdit(fi_id) {
    var type = document.forms["form-edit"]["type"].value;
    var subj = document.forms["form-edit"]["title"].value;
    var desc = document.forms["form-edit"]["comments"].value;
    var lat = document.forms["form-edit"]["latitude"].value;
    var long = document.forms["form-edit"]["longitude"].value;
    var imgs = document.forms["form-edit"]["image"].value;
    var vids = document.forms["form-edit"]["video"].value;
    var others = document.forms["form-edit"]["other"].value;


    var location = lat + ";" + long;

    // the upload code goes here
}

function saveChangeStatus(fi_id) {
    var status = document.forms["form-admin-details"]["status"].value;

    //code for undating goes here
}

function logout() {
    // some logic for logging out e.g clearing cookies and others
    window.location.replace("../index.html");
}