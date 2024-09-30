//제이쿼리 선언
$(function(){
    $("#searchBtn").click(function(){
        alert("검색버튼클릭")
        let surl="https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=YVh7Z42sgIoNX88ZIrqFPcu%2Fqs6%2BDxBeWbR7wbohbLDDwK%2FBX0gGNkRrOoLLLEQVLGGI%2BJLX2KUbWvNUBs9HlA%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
        let searchWord = $("#search_txt").val();
        surl += searchWord;
        $.ajax({
            url:surl,
            type:"get",
            data:"",
            dataType:"json",
            success:function(data){
                console.log(data.response.body.items.item);
                var g_item = data.response.body.items.item;
                console.log(g_item[0].galTitle)

                var h_data ="";
                for(var i=0;i<g_item.length;i++){

                    h_data +=`<tr>`;
                    h_data +=`<td>${g_item[i].galContentId}</td>`;
                    h_data +=`<td>${g_item[i].galTitle}</td>`;
                    h_data +=`<td>${g_item[i].galPhotographer}</td>`;
                    h_data +=`<td>${g_item[i].galModifiedtime}</td>`;
                    h_data +=`<td><img src='${g_item[i].galWebImageUrl}'</td>`;
                    h_data +=`<tr>`;

                }
                console.log(h_data);
                $("#tbody").html(h_data);
            },
            error:function(){
                alert("실패");
            }
    
        })
    })
})