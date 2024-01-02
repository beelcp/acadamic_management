
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
        document.getElementById('spinner'+id).className="fa fa-spinner";
        document.getElementById("department_id").value=id;

        $.ajax({
            type: "GET",
            url: document.getElementById("url_name").value,
            
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
                document.getElementById("status").value=data.status;
                console.log(data.status);
                $("modal_basic").show();
                document.getElementById('spinner'+id).className="fa fa-pencil";


            },

            error: function (error) {
                // Handle errors
                console.log(error);
            }
        });
    }
    
   
    
    
    function update_row() {
        var id = document.getElementById("department_id").value;
        var department_name = document.getElementById("department_name").value;
        var department_code = document.getElementById("department_code").value;
        var status = document.getElementById("status").value;
    
        $.ajax({
            type: "GET",
            url: document.getElementById("url_update").value,
            data: {
                'id': id,
                'department_name': department_name,
                'department_code': department_code,
                'status': status
            },
            dataType: "json",
            success: function (data) {
                if (data.success != '') {
                    alert(data.success);
                    $("#modal_basic").modal("hide");
                    window.location.reload(true);
                } else {
                    alert(data.error);
                }
            },
            error: function (error) {
                console.error('error occurred:', error);
            }
        });
    }
    
    function delete_row1(id) {
        var box = $("#mb-remove-row");
        box.addClass("open");
    
        box.find(".mb-control-yes").on("click", function () {
            box.removeClass("open");
    
            // Assuming you're using AJAX to send a POST request to the Django view
            $.ajax({
                type: "GET",
                url: document.getElementById("url_delete").value,
                data: {
                    'id': id,
                    
                },
                dataType: "json",
                success: function (data) {
                    if (data.success) {
                        $("#" + id).hide("slow", function () {
                            $(this).remove();
                        });
                        // Handle success (e.g., refresh the page or update the UI)
                    
                    } else {
                        // Handle error (e.g., display an error message)
                        alert(data.error);
                    }
                },
                error: function (error) {
                    console.error('Error occurred:', error);
                }
            });
        });
    }
    