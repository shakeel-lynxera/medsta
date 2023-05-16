$(document).ready(function(){

    //hide default div
    $("#profile-title-div").hide();
    $("#profile-about-div").hide();


//on click events//


    //on click of edit button basic info of profile
    $("#profile-basic-information-edit-btn").click(function(){
        $("#profile-basic-form").fadeIn(1000);
        $("#profile-basic-form").removeAttr('hidden');
        $("#profile-basic-information-cancel-btn").removeAttr('hidden');
        $("#profile-basic-information-edit-btn").hide();
        $("#profile-basic-information-details").hide();
    });

    //on click of cancel button basic info of profile
    $("#profile-basic-information-cancel-btn").click(function(){
        $("#profile-basic-form").attr('hidden', 'hidden');
        $("#profile-basic-information-cancel-btn").attr('hidden', 'hidden');
        $("#profile-basic-information-edit-btn").show();
        $("#profile-basic-information-details").fadeIn(1000);
        $("#profile-basic-information-details").show();
    });

    //onclick event for the edit button profile title
    $("#profile-title-edit-btn").click(function(){
        $('#profile-title-input').removeAttr('hidden');
        $('#profile-title-save-btn').removeAttr('hidden');
        $('#profile-title-cancel-btn').removeAttr('hidden');
        $("#profile-title-div").fadeIn(1000);
        $("#profile-title-input").focus();
        $("#profile-title-input").val($("#profile-title").text());
        $("#profile-title").hide();
        $("#profile-title-edit-btn").hide();
    });

    //onclick event for the cancel button profile title
    $("#profile-title-cancel-btn").click(function(){
        $('#profile-title-input').attr('hidden', 'hidden');
        $('#profile-title-save-btn').attr('hidden', 'hidden');
        $('#profile-title-cancel-btn').attr('hidden', 'hidden');
        $("#profile-title-div").fadeOut(1000);
        $("#profile-title").fadeIn(1000);
        $("#profile-title-edit-btn").fadeIn(1000);
    });

    //onclick event for the edit about profile
    $("#profile-about-edit-btn").click(function(){
        $("#static-profle-about").hide();
        $('#profile-about-input').removeAttr('hidden');
        $('#profile-about-save-btn').removeAttr('hidden');
        $('#profile-about-cancel-btn').removeAttr('hidden');
        $("#profile-about-div").fadeIn(1000);
        $("#profile-about-input").focus();
        $("#profile-about-input").val($("#profile-about").text());
        $("#profile-about").hide();
        $("#profile-about-edit-btn").hide();
    });

    //onclick event for the cancel about profile
    $("#profile-about-cancel-btn").click(function(){
        $("#static-profle-about").fadeIn(1000);
        $('#profile-about-input').attr('hidden', 'hidden');
        $('#profile-about-save-btn').attr('hidden', 'hidden');
        $('#profile-about-cancel-btn').attr('hidden', 'hidden');
        $("#profile-about-div").fadeOut(1000);
        $("#profile-about").fadeIn(1000);
        $("#profile-about-edit-btn").fadeIn(1000);
    });

    //skills
    $("#add-skill-text").click(function(){
        $("#add-skill-text").hide();
        $("#hide-skill-text").removeAttr('hidden');
        $("#add-skill-form").fadeIn(1000);
        $("#add-skill-form").removeAttr('hidden');
        $("#add-skill-controller").removeAttr('hidden');
    });

    $("#hide-skill-text").click(function(){
        $("#add-skill-text").show();
        $("#hide-skill-text").attr('hidden', 'hidden');
        $("#add-skill-form").attr('hidden', 'hidden');
        $("#add-skill-controller").attr('hidden', 'hidden');
    });


    //interets
    $("#add-interest-text").click(function(){
        $("#add-interest-text").hide();
        $("#hide-interest-text").removeAttr('hidden');
        $("#add-interest-form").fadeIn(1000);
        $("#add-interest-form").removeAttr('hidden');
        $("#add-interest-controller").removeAttr('hidden');
    });

    $("#hide-interest-text").click(function(){
        $("#add-interest-text").show();
        $("#hide-interest-text").attr('hidden', 'hidden');
        $("#add-interest-form").attr('hidden', 'hidden');
        $("#add-interest-controller").attr('hidden', 'hidden');
    });


    //languages
    $("#add-language-text").click(function(){
        $("#add-language-text").hide();
        $("#hide-language-text").removeAttr('hidden');
        $("#add-language-form").fadeIn(1000);
        $("#add-language-form").removeAttr('hidden');
        $("#add-language-controller").removeAttr('hidden');
    });

    $("#hide-language-text").click(function(){
        $("#add-language-text").show();
        $("#hide-language-text").attr('hidden', 'hidden');
        $("#add-language-form").attr('hidden', 'hidden');
        $("#add-language-controller").attr('hidden', 'hidden');
    });


//APIs call//

    //update profile title
    $("#profile-title-save-btn").click(function(){
        $("#profile-title-save-btn").addClass("disabled");
        var title = $("#profile-title-input").val();
        data = {"title":title}
        data =JSON.stringify(data);
        $.ajax(
        {
            type:"PUT",
            url: "/update_profile_title/",
            data:data,
            success: function( data ) {  
                $("#profile-title-save-btn").removeClass("disabled");
                $("#profile-title-div").hide();
                $("#profile-title").show();
                $("#profile-title-edit-btn").show();
                $("#profile-title").text(title);
                $("#static-profle-title").text(title);
            },
            error : function() {
                $("#profile-title-save-btn").removeClass("disabled");
                alert("error while loading data");
            }
         })
    });

    //update profile about
    $("#profile-about-save-btn").click(function(){
        $("#profile-about-save-btn").addClass("disabled");
        var about = $("#profile-about-input").val();
        data = {"about":about}
        data =JSON.stringify(data);
        $.ajax(
        {
            type:"PUT",
            url: "/update-profile-about/",
            data:data,
            success: function( data ) {  
                $("#profile-about-save-btn").removeClass("disabled");
                $("#profile-about-div").hide();
                $("#profile-about").show();
                $("#profile-about-edit-btn").show();
                $("#profile-about").text(about);
                $("#static-profle-about").text(about);
                $("#static-profle-about").show();
            },
            error : function() {
                $("#profile-about-save-btn").removeClass("disabled");
                alert("error while loading data");
            }
         })
    });


    //update experience
    $("#experience-save-btn").click(function(){
        var id =$("#xp-edit-id").val();
        var title = $("#xp-edit-title").val();
        var company =  $("#xp-edit-company").val();
        var start_date = $("#xp-edit-start-date").val();
        //$("#xp-edit-currently-working").val(currenlty_working);
        var end_date = $("#xp-edit-end-date").val();
        var location = $("#xp-edit-location").val();
        var description = $("#xp-edit-description").val();
        data = {"id":id,
                "title":title,
                "company":company,
                "start_date":start_date,
                "end_date":end_date,
                "location":location,
                "description":description}

        data =JSON.stringify(data);
        $.ajax(
        {
            type:"PUT",
            url: "/update-experience/",
            data:data,
            success: function( data ) {
                window.location.replace("http://50.19.158.239:8001/profile/");
            },
            error : function() {
                alert("error while loading data");
            }
         })
    });

    //delete experience
    $("#experience-delete-btn").click(function(){
        var id =$("#xp-edit-id").val();
        $.ajax(
        {
            type:"DELETE",
            url: "/delete-experience/"+id+"/",
            success: function( data ) {
                window.location.replace("http://50.19.158.239:8001/profile/");
            },
            error : function() {
                alert("error while loading data");
            }
            })
        });
    
    //cancel experience
    $("#experience-cancel-btn").click(function(){
        $("#div-edit-experience").attr('hidden', 'hidden');
    });


    //update accomplishment
    $("#accomplishment-save-btn").click(function(){
        var id =$("#accomplishment-edit-id").val();
        var title = $("#accomplishment-edit-title").val();
        var description =  $("#accomplishment-edit-description").val();
        var start_date = $("#accomplishment-edit-start-date").val();
        var end_date = $("#accomplishment-edit-end-date").val();
        var visit_url = $("#accomplishment-edit-visit-url").val();
        data = {"id":id,
                "title":title,
                "description":description,
                "start_date":start_date,
                "end_date":end_date,
                "visit_url":visit_url
                }
        data = JSON.stringify(data);
        $.ajax(
        {
            type:"PUT",
            url: "/update-accomplishment/",
            data:data,
            success: function( data ) {
                window.location.replace("http://50.19.158.239:8001/profile/");
            },
            error : function() {
                alert("error while loading data");
            }
            })
        });

    //delete accomplishment
    $("#accomplishment-delete-btn").click(function(){
        var id =$("#accomplishment-edit-id").val();
        $.ajax(
        {
            type:"DELETE",
            url: "/delete-accomplishment/"+id+"/",
            success: function( data ) {
                window.location.replace("http://50.19.158.239:8001/profile/");
            },
            error : function() {
                alert("error while loading data");
            }
        })
    });

    //cancel accomplishment
    $("#accomplishment-cancel-btn").click(function(){
        $("#div-edit-accomplishment").attr('hidden', 'hidden');
    });
        
    
    //edit skill
    $("#skill-edit-btn").click(function(){
        $("#skill-edit-btn").hide();
        $("#skill-cancel-edit-btn").removeAttr('hidden');
        $(".skill-trash-icons").removeAttr('hidden');
    });

    //cancel skill edit
    $("#skill-cancel-edit-btn").click(function(){
        $("#skill-edit-btn").show();
        $("#skill-cancel-edit-btn").attr('hidden', 'hidden');
        $(".skill-trash-icons").attr('hidden', 'hidden');
    });

    //edit interest
    $("#interest-edit-btn").click(function(){
        $("#interest-edit-btn").hide();
        $("#interest-cancel-edit-btn").removeAttr('hidden');
        $(".interest-trash-icons").removeAttr('hidden');
    });

    //cancel interest edit
    $("#interest-cancel-edit-btn").click(function(){
        $("#interest-edit-btn").show();
        $("#interest-cancel-edit-btn").attr('hidden', 'hidden');
        $(".interest-trash-icons").attr('hidden', 'hidden');
    });


    //edit language
    $("#language-edit-btn").click(function(){
        $("#language-edit-btn").hide();
        $("#language-cancel-edit-btn").removeAttr('hidden');
        $(".language-trash-icons").removeAttr('hidden');
    });

    //cancel language edit
    $("#language-cancel-edit-btn").click(function(){
        $("#language-edit-btn").show();
        $("#language-cancel-edit-btn").attr('hidden', 'hidden');
        $(".language-trash-icons").attr('hidden', 'hidden');
    });


    //______________________________________Network Management_________________________________________

    // Requested People
    $("#friend-requests-li").click(function(){
        $("#div-friend-requests").removeAttr('hidden');
        $("#div-people-suggeseted").attr('hidden', 'hidden');
        $("#div-people-connection").attr('hidden', 'hidden');
        $("#div-invitations").attr('hidden', 'hidden');
        $("#friend-requests-li").addClass('active');
        $("#people-invited-li").removeClass('active');
        $("#people-suggeseted-li").removeClass('active');
        $("#people-connected-li").removeClass('active');
    });

    // People Suggeseted
    $("#people-suggeseted-li").click(function(){
        $("#div-people-suggeseted").removeAttr('hidden');
        $("#div-friend-requests").attr('hidden', 'hidden');
        $("#div-people-connection").attr('hidden', 'hidden');
        $("#div-invitations").attr('hidden', 'hidden');
        $("#people-suggeseted-li").addClass('active');
        $("#people-invited-li").removeClass('active');
        $("#friend-requests-li").removeClass('active');
        $("#people-connected-li").removeClass('active');
    });

    // People Invited
    $("#people-invited-li").click(function(){
        $("#div-invitations").removeAttr('hidden');
        $("#div-people-suggeseted").attr('hidden', 'hidden');
        $("#div-friend-requests").attr('hidden', 'hidden');
        $("#div-people-connection").attr('hidden', 'hidden');
        $("#people-invited-li").addClass('active');
        $("#people-suggeseted-li").removeClass('active');
        $("#friend-requests-li").removeClass('active');
        $("#people-connected-li").removeClass('active');
    });

    // People Connected

    $("#people-connected-li").click(function(){
        $("#div-people-connection").removeAttr('hidden');
        $("#div-people-suggeseted").attr('hidden', 'hidden');
        $("#div-friend-requests").attr('hidden', 'hidden');
        $("#div-invitations").attr('hidden', 'hidden');
        $("#people-connected-li").addClass('active');
        $("#people-invited-li").removeClass('active');
        $("#people-suggeseted-li").removeClass('active');
        $("#friend-requests-li").removeClass('active');
    });

});

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
}

function edit_experience(title, company, start_date, currenlty_working, end_date, location, description, id){
    $("#div-edit-experience").fadeIn(1000);
    $("#div-edit-experience").removeAttr('hidden');
    $("#xp-edit-id").val(id);
    $("#xp-edit-title").val(title);
    $("#xp-edit-company").val(company);

    var today = new Date(start_date);
    var d = (today.getDate() < 10 ? '0' : '' )+ today.getDate();
    var m = ((today.getMonth() + 1) < 10 ? '0' :'') + (today.getMonth() + 1);
    var y = today.getFullYear();
    var x = String(y+"-"+m+"-"+d); 

    $("#xp-edit-start-date").val(x);
    //$("#xp-edit-currently-working").val(currenlty_working);
    $("#xp-edit-end-date").val(end_date);
    $("#xp-edit-location").val(location);
    $("#xp-edit-description").val(description);
    //$("#xp-edit-id").val(id);
}

function edit_accomplishment(title, start_date, end_date, description, visit_url, id){
    $("#div-edit-accomplishment").fadeIn(1000);
    $("#div-edit-accomplishment").removeAttr('hidden');
    $("#accomplishment-edit-id").val(id);
    $("#accomplishment-edit-title").val(title);
    $("#accomplishment-edit-start-date").val(start_date);
    $("#accomplishment-edit-end-date").val(end_date);
    $("#accomplishment-edit-description").val(description);
    $("#accomplishment-edit-visit-url").val(visit_url);
}

function delete_skill(id){
    $.ajax(
    {
        type:"DELETE",
        url: "/delete-skill/"+id+"/",
        success: function( data ) {
            window.location.replace("http://50.19.158.239:8001/profile/");
        },
        error : function() {
            alert("error while loading data");
        }
    })
}

function delete_interest(id){
    $.ajax(
    {
        type:"DELETE",
        url: "/delete-interest/"+id+"/",
        success: function( data ) {
            window.location.replace("http://50.19.158.239:8001/profile/");
        },
        error : function() {
            alert("error while loading data");
        }
    })
}

function delete_language(id){
    $.ajax(
    {
        type:"DELETE",
        url: "/delete-language/"+id+"/",
        success: function( data ) {
            window.location.replace("http://50.19.158.239:8001/profile/");
        },
        error : function() {
            alert("error while loading data");
        }
    })
}


function send_connect_request(id, btn){
    btn.disabled = true;
    $.ajax(
        {
            type:"POST",
            url: "/send-connect-request/"+id+"/",
            success: function( data ) {
                btn.value = "Request Sent";
        },
        error : function(e) {
            btn.disabled = false;
            alert("error while loading data");
        }
    })
}

function cancel_connect_request(id, btn){
    btn.disabled = true;
    $.ajax(
        {
            type:"DELETE",
            url: "/cancel-connect-request/"+id+"/",
            success: function( data ) {
                btn.value = "Canceled";
        },
        error : function(e) {
            btn.disabled = false;
            alert("error while loading data");
        }
    })
}

function accept_friend_request(id, btn){
    accept_btn = document.getElementById("accept-friend-request-btn-"+id)
    reject_btn = document.getElementById("reject-friend-request-btn-"+id)
    accept_btn.disabled = true;
    reject_btn.disabled = true;
    $.ajax(
        {
            type:"POST",
            url: "/accept-friend-request/"+id+"/",
            success: function( data ) {
                accept_btn.value = "Accepted";
                reject_btn.style.display = "none";
        },
        error : function(e) {
            accept_btn.disabled = false;
            reject_btn.disabled = false;
            alert("error while loading data");
        }
    })
}


function reject_friend_request(id, btn){
    accept_btn = document.getElementById("accept-friend-request-btn-"+id)
    reject_btn = document.getElementById("reject-friend-request-btn-"+id)
    accept_btn.disabled = true;
    reject_btn.disabled = true;
    $.ajax(
        {
            type:"DELETE",
            url: "/reject-friend-request/"+id+"/",
            success: function( data ) {
                reject_btn.value = "Cancled";
                accept_btn.style.display = "none";
        },
        error : function(e) {
            accept_btn.disabled = false;
            reject_btn.disabled = false;
            alert("error while loading data");
        }
    })
}


//smoth moving (MAY ADD LATER)
// $(document).on('click', 'a[href^="#"]', function (event) {
//     event.preventDefault();

//     $('html, body').animate({
//         scrollTop: $($.attr(this, 'href')).offset().top
//     }, 1000);
// });