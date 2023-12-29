
    function delete_row(row){
        
        var box = $("#mb-remove-row");
        box.addClass("open");
        
        box.find(".mb-control-yes").on("click",function(){
            box.removeClass("open");
            $("#"+row).hide("slow",function(){
                $(this).remove();
            });
        });
        
    }
 
    // function edit_row(id){
        

    //     $.ajax({
    //         type: "POST",
    //         url: "{% url 'ajaxsend' %}",
    //         data: {
    //             'name': id
    //         },
    //         dataType: "json",
    //         success: function (data) {
    //             // Handle the successful response
    //             alert(data.message + "\nData 1 from client:" + data.name + "\nData 2 from client: ");
    //         },
    //         error: function (error) {
    //             // Handle errors
    //             console.log(error);
    //         }
    //     });

    // }

   

    function edit_row(id) {
        
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/ajax_department_view/",
            data : {
                'id': id
            },
        
            dataType: "json",
            success: function (data) {
                // Handle the successful response
                // alert(data.message + "\nDepartment Name: " + data.department_name +
                //       "\nDepartment Code: " + data.department_code +
                //       "\nStatus: " + (data.status ? 'Active' : 'Inactive'));
                document.getElementById("department_name").value=data.department_name;
                document.getElementById("department_code").value=data.department_code;
                $("modal_basic").show();

            },
            error: function (error) {
                // Handle errors
                console.log(error);
            }
        });
    }
    