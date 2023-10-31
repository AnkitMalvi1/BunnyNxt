 
   
  $(".single-login").on("click", function() {
    
   
  }); 

 

  // const shareData = {
  //   title: 'MDN',
  //   text: 'Learn web development on MDN!',
  //   url: 'https://developer.mozilla.org'
  // }
  
  // const btn = document.querySelector('.button');
  // const resultPara = document.querySelector('.result');
  
  // // Share must be triggered by "user activation"
  // btn.addEventListener('click', async () => {
  //   try {
  //     await navigator.share(shareData)
  //     resultPara.textContent = 'MDN shared successfully'
  //   } catch (err) {
  //     resultPara.textContent = `Error: ${err}`
  //   }
  // });

  $("#downloadRingtone").click( function () {
       
    ringtoneid = $("#download_count").val()
    console.log("working")
      $.ajax({
        url: "/incrementUrl/",
        dataType: "json",
        type: "POST",
        data: JSON.stringify({
          ringtone_id: ringtoneid,
        }),
        processData: !1,
        success: function (res) {
          console.log(res)
          $("#downloadCount").text(res['download']);
        },
      });
  });

  $("#sharecount").on('click',function () {

    navigator.share({
      url: document.URL,
      title: document.title,
      text: "lorem ipsum..."
    });   
    ringtoneid = $("#download_count").val()
    console.log("working")
      $.ajax({
        url: "/sharecount/",
        dataType: "json",
        type: "POST",
        data: JSON.stringify({
          ringtone_id: ringtoneid,
        }),
        processData: !1,
        success: function (res) {
          console.log(res)
          $("#sharenumber").text(res['share']);
        },
      });
  });

  // $(document).ready(function () {
    
    $("#like-ract").click( function () {
      if (user_ckeck == 'True') {
      ringtoneid = $("#download_count").val()
      console.log("working")
        $.ajax({
          url: "/ringtonelike/",
          type: "POST",
          data: {
            ringtone_id: ringtoneid,
          },
          success: function (res) {
            $("#nol").text(res['tl']);



            $("#nol").text(res['tl']);
            if (res['result'] == true){
              var heart = $(".big-heart-an") 

                heart.addClass('fade-in');

                setTimeout(function() {
                    heart.removeClass('fade-in').animate({
                      transition: "1s linear"
                    })
                }, 1000);


              $("#likesvg").html(`<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M23.3783 2.85143C20.7425 -0.728842 16.0069 -0.933429 13.1924 2.33997C12.7903 2.80029 12.1649 2.80029 11.8075 2.33997C9.12697 -0.779989 4.70415 -0.779989 2.02365 2.33997C-0.299449 4.94845 -0.656849 9.19364 1.13015 12.3136C1.66625 13.2854 2.38105 14.0526 3.14053 14.6152L12.0308 22.8498C12.3436 23.1567 12.7903 23.1567 13.103 22.8498L21.9487 14.6152C22.7082 14.0526 23.3783 13.3365 23.9144 12.3647C25.5227 9.44938 25.344 5.51107 23.3783 2.85143V2.85143Z" fill="#FF473E"/>
              </svg>`);
            }
            else{
              $("#likesvg").html(`<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M17.3435 0.000429746C16.3369 0.0107839 15.3044 0.207346 14.2943 0.610534L14.2485 0.629992L14.2026 0.653617C13.5623 0.979701 12.9787 1.38762 12.4599 1.87103C9.66776 -0.543904 5.22253 -0.719174 2.18137 2.02251L2.15078 2.0503L2.12299 2.07949C-0.544841 4.86608 -0.482362 9.15756 1.1168 12.5484L1.1307 12.5748L1.1446 12.6026C3.02801 16.0903 6.54493 19.0537 9.74989 21.4901L9.75822 21.497L9.76516 21.5026C9.97135 21.6537 10.3259 21.9663 10.7352 22.2739C11.1445 22.5815 11.6068 22.9186 12.2834 23.048L12.4348 23.0771L12.5877 23.0646C13.2978 23.0034 13.5763 22.7412 14.0428 22.4476C14.5093 22.1539 15.0256 21.7812 15.5562 21.3733C16.6021 20.5692 17.6843 19.6425 18.3969 18.9816C18.406 18.973 18.4212 18.9608 18.4302 18.9524C18.4317 18.9511 18.4329 18.9495 18.4344 18.9482C19.9355 17.6673 21.4224 16.1907 22.6828 14.4538C22.6832 14.4533 22.6838 14.4529 22.6842 14.4524C22.6866 14.4492 22.6888 14.4459 22.6912 14.4427C24.6902 11.7512 25.66 8.12403 24.5034 4.55049L24.4825 4.48656L24.4547 4.42678C23.1562 1.61941 20.3632 -0.0305911 17.3435 0.000429746ZM17.3796 2.19901C19.5553 2.14897 21.4624 3.31397 22.4091 5.30647C23.2839 8.09599 22.5277 10.9381 20.8984 13.1266L20.8942 13.1321L20.8901 13.1377C19.7551 14.704 18.3805 16.075 16.9557 17.2875L16.9377 17.3042L16.9196 17.3208C16.278 17.9181 15.192 18.8484 14.1999 19.6111C13.7038 19.9925 13.2282 20.3333 12.8588 20.5659C12.7198 20.6533 12.5878 20.713 12.4793 20.7591C12.3654 20.6968 12.2208 20.6091 12.0708 20.4964C11.7687 20.2694 11.447 19.9796 11.0966 19.7209C11.0911 19.7168 11.0853 19.7126 11.0799 19.7084C7.9696 17.3427 4.69343 14.4702 3.11803 11.5742C1.83905 8.84187 1.89487 5.57147 3.70172 3.64989C6.15851 1.46547 9.80845 1.94037 11.6288 4.18216L12.5155 5.27312L13.373 4.15993C13.8663 3.51987 14.4551 3.03055 15.1699 2.65901C15.9191 2.36633 16.6635 2.21547 17.3796 2.19901Z" fill="#D9D9D9"/>
              </svg>`);
            }

            
            
           
            
          },
        });

      }else{
        url = "/login/"
    $(location).attr('href',url);
    console.log("else woking")
      }
    });
    
   
      
   

    $(".ringtone-bg-image").dblclick( function () {
      if (user_ckeck == 'True') {
        ringtoneid = $("#download_count").val()
        console.log("working")
        $.ajax({
          url: "/ringtonelikefull/",
          type: "POST",
          data: {
            ringtone_id: ringtoneid,
          },
          success: function (res) {
            $("#nol").text(res['tl']);
            if (res['result'] == true){
              var heart = $(".big-heart-an") 

                heart.addClass('fade-in');

                setTimeout(function() {
                    heart.removeClass('fade-in').animate({
                      transition: "1s linear"
                    })
                }, 1000);


              $("#likesvg").html(`<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M23.3783 2.85143C20.7425 -0.728842 16.0069 -0.933429 13.1924 2.33997C12.7903 2.80029 12.1649 2.80029 11.8075 2.33997C9.12697 -0.779989 4.70415 -0.779989 2.02365 2.33997C-0.299449 4.94845 -0.656849 9.19364 1.13015 12.3136C1.66625 13.2854 2.38105 14.0526 3.14053 14.6152L12.0308 22.8498C12.3436 23.1567 12.7903 23.1567 13.103 22.8498L21.9487 14.6152C22.7082 14.0526 23.3783 13.3365 23.9144 12.3647C25.5227 9.44938 25.344 5.51107 23.3783 2.85143V2.85143Z" fill="#FF473E"/>
              </svg>`);
            }
            else{
              $("#likesvg").html(`<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M17.3435 0.000429746C16.3369 0.0107839 15.3044 0.207346 14.2943 0.610534L14.2485 0.629992L14.2026 0.653617C13.5623 0.979701 12.9787 1.38762 12.4599 1.87103C9.66776 -0.543904 5.22253 -0.719174 2.18137 2.02251L2.15078 2.0503L2.12299 2.07949C-0.544841 4.86608 -0.482362 9.15756 1.1168 12.5484L1.1307 12.5748L1.1446 12.6026C3.02801 16.0903 6.54493 19.0537 9.74989 21.4901L9.75822 21.497L9.76516 21.5026C9.97135 21.6537 10.3259 21.9663 10.7352 22.2739C11.1445 22.5815 11.6068 22.9186 12.2834 23.048L12.4348 23.0771L12.5877 23.0646C13.2978 23.0034 13.5763 22.7412 14.0428 22.4476C14.5093 22.1539 15.0256 21.7812 15.5562 21.3733C16.6021 20.5692 17.6843 19.6425 18.3969 18.9816C18.406 18.973 18.4212 18.9608 18.4302 18.9524C18.4317 18.9511 18.4329 18.9495 18.4344 18.9482C19.9355 17.6673 21.4224 16.1907 22.6828 14.4538C22.6832 14.4533 22.6838 14.4529 22.6842 14.4524C22.6866 14.4492 22.6888 14.4459 22.6912 14.4427C24.6902 11.7512 25.66 8.12403 24.5034 4.55049L24.4825 4.48656L24.4547 4.42678C23.1562 1.61941 20.3632 -0.0305911 17.3435 0.000429746ZM17.3796 2.19901C19.5553 2.14897 21.4624 3.31397 22.4091 5.30647C23.2839 8.09599 22.5277 10.9381 20.8984 13.1266L20.8942 13.1321L20.8901 13.1377C19.7551 14.704 18.3805 16.075 16.9557 17.2875L16.9377 17.3042L16.9196 17.3208C16.278 17.9181 15.192 18.8484 14.1999 19.6111C13.7038 19.9925 13.2282 20.3333 12.8588 20.5659C12.7198 20.6533 12.5878 20.713 12.4793 20.7591C12.3654 20.6968 12.2208 20.6091 12.0708 20.4964C11.7687 20.2694 11.447 19.9796 11.0966 19.7209C11.0911 19.7168 11.0853 19.7126 11.0799 19.7084C7.9696 17.3427 4.69343 14.4702 3.11803 11.5742C1.83905 8.84187 1.89487 5.57147 3.70172 3.64989C6.15851 1.46547 9.80845 1.94037 11.6288 4.18216L12.5155 5.27312L13.373 4.15993C13.8663 3.51987 14.4551 3.03055 15.1699 2.65901C15.9191 2.36633 16.6635 2.21547 17.3796 2.19901Z" fill="#D9D9D9"/>
              </svg>`);
            }

            
            
           
            
          },
        });
      }else{
        url = "/login/"
    $(location).attr('href',url);
    console.log("else woking")
      }
      
        
    })
   
  // }else{

  //   url = "/login/"
  //   $(location).attr('href',url);
  // }
  
  // if (user_ckeck == true) {
     
  // }
  // else{

  //   url = "/login/"
  //   $(location).attr('href',url);
  // }
 
 
 
 

 

// Play Function
$(".player").on(
    "click",
    ".play-action .play-btn .home-play-btn",
    function (current) {
     st = $(this).parent().parent().find(".ring-preloader").css('display', 'inline-flex');
    //  console.log(st)
      $(this).css("display", "none");
       
      $(".home-play-btn")
        .not(this)
        .parent()
        .find(".home-pause-btn")
        .css("display", "none");
      $(".home-play-btn")
        .not(this)
        .parent()
        .find(".home-play-btn")
        .css("display", "inline-flex");
  
  
        $(".home-play-btn")
        .not(this)
        .parent()
        .find(".ring-preloader")
        .css("display", "none");
      // $(".home-play-btn")
      //   .not(this)
      //   .parent()
      //   .find(".home-play-btn")
      //   .css("display", "inline-block");
  
  
      // ADD / REMOVE CLASS
      $(".related-ringtone-item").addClass("isPlaying");
       
      // $(this).addClass("isPlaying");
      $(".home-play-btn").not(this).parent().parent().parent().removeClass("isPlaying");
  
      $("audio").each(function (e) {
        if (e !== current.currentTarget) {
          $(this)[0].pause();
          // $(this)[0].currentTime = 0;
          // $(this).parent().parent().parent().find(".ring-progress").css("width",  "0")
        }
      });
      ad = $(this).parent().parent().find(".track audio")[0]
      
   
       current_time = $(this).parent().parent().find(".track audio")[0].duration;
  
      console.log(current_time)
     
      total_duration = formatTime(ad.duration)     
      
      // $('.timeline').on('click', function(e){
      //   if (audios.src) {
      //     percent = e.offsetX / this.offsetWidth;
      //     audios.currentTime = percent * player.duration;
      //     // update progress bar
      //     $('.progress').css('width', Math.floor(percent / 100)+'%');
      //   }
      // });
      
    
  
      if ($(this).parent().parent().find(".track audio")[0].play()) {

         
        ringtoneid = $(ad).data('id')
        // $(".music-svg #div").css("display", "flex")
        // $(".music-svg svg").css("display", "none")


        ringtone = $(this).parent().parent().find('.played span') 
        console.log(ringtoneid)
        
        $.ajax({
                method:"POST",
                url:"/ringtone_played/",
                
                data:{
                  ringtoneid:ringtoneid,
                  csrfmiddlewaretoken:token
                },
                 
                success: function(response){
                   
                   
                    
                    console.log(response)
                    if (response['sucess']){


                      $(ringtone).text(response['sucess'])
                      $(`#post${ringtoneid}`).text(response['sucess'])
                        
                    
                    }
                     
                },
                complete:function(data){
            $('#step1-btn').text("CONTINUE") 
            $('#step1-btn').prop('disabled', false);  
                 
            }
                
            })
  
        ad.onplaying = function(){
          st1 = $(this).parent().parent().parent().find(".ring-preloader").hide();
          // $(this).parent().find(".home-pause-btn").css("display", "inline-block");
          // console.log(st1)
          st2 = $(this).parent().parent().find(".home-pause-btn").css("display", "inline-flex");

          
          //  console.log(st2)
         }

        
          
          
        
        $($(this).parent().parent().find(".track audio")[0]).on('timeupdate' ,function(){
  
           
          value = Math.floor((100 / ad.duration) * ad.currentTime);
            
          // val2 = (ad.currentTime / ad.duration *100 + "%")
            ct_du = formatTime(ad.currentTime)
          console.log($(this).parent().parent().find(".track audio")[0])
            
          // rect = $('.ringtone-player')[0].getBoundingClientRect();
  
          // rect1 = $('.timeline')[0].getBoundingClientRect();
        //  console.log(value)
           
        //   percentage = ad.currentTime / ad.duration;
  
        //   main = percentage * rect.width;
        //   main1 = percentage * rect1.width;
  
          $(this).parent().parent().parent().find(".ring-progress").css("width", value + '%')
          // console.log(value)

          // riid = $("#riid").data('id')
          // console.log(riid)
          // if (riid){
          //   eli = $('.progress').css("width", value + '%')
          // }
          
  
          //  eli1 = $(this).parent().parent().parent().parent().find('.current').text(ct_du)
          //  eli = $(this).parent().parent().parent().parent().find('.length').text(total_duration)
           
          // $('#len').text(dur)
           
        });
        
  
  
        
        // $($(this).parent().parent().find(".track audio")[0]).on('waiting' ,function(){
        //   st1 = $(this).parent().parent().parent().find(".lenl").hide();
        //   $(this).parent().find(".home-pause-btn").css("display", "inline-block");
        //   console.log(st1)
        //   st2 = $(this).parent().parent().find(".home-pause-btn").css("display", "inline-block");
        //    console.log(st2)
           
        // });
        
  
         
         
  
        
         
           
        
           
           
         
        
         
  
        
  
        $(".audio1").on("ended", function (current) {
          $(".play-action .play-btn .home-pause-btn").css("display", "none");
          $(".play-action .play-btn .home-play-btn").css(
            "display",
            "inline-flex"
          );
  
  
          $(this).parent().parent().parent().find(".ring-progress").css("width",  "0")
        });
      }
  
       
  
  
      
      value = Math.floor((100 / ad.duration) * ad.currentTime);
        
       
      
  
    
    // if(audio.readyState > 0)  {
      
      
    //   alert(minutes+":"+seconds);
    // }
    //     value = Math.floor((100 / ad.duration) * ad.currentTime);
    //     $(this).parent().parent().find(".ring-progress").css("width", value+ '%')
       
  
      // progress1 = $('.progress1');
  
      // current_time = $(this).parent().parent().find(".track audio")[0].play().currentTime;
      
      // $('.categoryName').text()
  
  
    }
  
  
     
  
    
  
    // if($(audio.readyState > 0))  {
    //   var minutes = parseInt(audio.duration / 60, 10);
    //   var seconds = parseInt(audio.duration % 60);
      
    //   alert(minutes+":"+seconds);
    // } 
  );
  
  // if ((audio.readyState > 0)){
  
  // });
   
  
  
  
  // PAUSE FUNCTION 
  $(".player").on(
    "click",
    ".play-action .play-btn .home-pause-btn",
    function () {
      // HIDE PASE ICON
      $(this).parent().find(".home-pause-btn").css("display", "none");
      // Show Play Icon
      $(this).parent().find(".home-play-btn").css("display", "inline-flex");
      // PAUSE AUDIO TRACK
      $(this).parent().parent().find(".track audio")[0].pause();
    }
  );
//  $(document).ready(function () {

//     console.log("??????????????")
//     $("#riid").play() = function(){
//       // st1 = $(this).parent().parent().parent().find(".ring-preloader").hide();
//       // $(this).parent().find(".home-play-btn").css("display", "inline-block");
//       console.log('////')
//       // st2 = $(this).parent().parent().find(".home-pause-btn").css("display", "inline-flex");
//       // //  console.log(st2)
//      }
      
//   })
  
  
  
  
  // $(audios) .on('loadedmetadata' ,function(){
  //   eli111 = $('.length').text(audios.duration)
  //   console.log(eli111)
  
   
  //     alert(audios.duration);
  //     // console.log(audio[0].duration)
   
  // });
  
  // $(audios).on("loadedmetadata", function() {
  //   alert(audios.duration);
  //   console.log(audios.duration)
  // }); 
  
  
  // $(audios).on('durationchange', function(){
  //   var duration = audios.duration;
  //   alert(audios.duration);
  //   if(!isNaN(duration)) {
  //       $('.length').html(Math.ceil(duration));
  //   }
  // });
  
  // document.addEventListener('DOMContentLoaded', function(event){
  // function runWhenLoaded() { /* read duration etc, this = audio element */ }
  
  // if (!audios.readyState) { // or $audio[0].readyState
  //     audios.addEventListener("loadedmetadata", runWhenLoaded);
  //     // or $audio.on("loadedmetadata", runWhenLoaded);
  //     alert(audios.duration);
  // } else {
  //     runWhenLoaded.call(audios);
  //     // or runWhenLoaded.call($audio[0]);
  //     alert(audios.duration);
  // }
  // });
  // if ($('.ringtone-player').hasClass('isPlaying')){
  //   $('.isPlaying').find('*').css('color', 'white')
  // } else{
  //   $('.isPlaying').find('*').css('color', 'red')
  // }
  
  
  // if (audios.readyState > 0) {
  //   // alert(audios.duration);
  //   $('.length').text(formatTime(audios.duration));
  // } else {
  //   $(audios).on('loadedmetadata', function(){
  //     $('.length').text(formatTime(audios.duration));
  //     // alert(audios.duration);
  //   });
  // }
  // // $('.length').text()
  
  
  function formatTime(time) {
    var min = Math.floor(time / 60);
    var sec = Math.floor(time % 60);
    return min + ':' + (sec < 10 ? '0' + sec : sec);
  }
  
   
  // $(".download_info a:first-child").prepend($('.android-svg').css('display','block'))
  // $(".download_info a:last-child").prepend($('.ios-svg').css('display','block'))
// })


$($(".single-ring-play .track audio")[0]).on('timeupdate' ,function(){
  newad = $(".single-ring-play .track audio")[0]
    
  
  rect1 = $('.timeline')[0].getBoundingClientRect();
        
           
  percentage = newad.currentTime / newad.duration;

  main1 = percentage * rect1.width;
  
  console.log(rect1.width)
  console.log(main1)
  
  value = Math.floor((100 / newad.duration) * newad.currentTime);
  
    
  
     $('.progress').css("width", main1 + 'px')
  
  
   
});

// $(window).on("load",function(){
//   $(".loader-container").fadeOut(1000);
// });
