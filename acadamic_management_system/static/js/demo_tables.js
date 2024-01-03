
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
        // department
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
    
    function edit_desrow(id) {
         // designation
        document.getElementById('spinner' + id).className = "fa fa-spinner";
        document.getElementById("designation_id").value = id;  // Change 'department_id' to 'designation_id'
    
        $.ajax({
            type: "GET",
            url: document.getElementById("url_name").value,
    
            data: {
                'id': id
            },
    
            dataType: "json",
            success: function (data) {
                // Handle the successful response
                // alert(data.message + "\nDesignation Name: " + data.designation_name +
                //       "\nDesignation Code: " + data.designation_code +
                //       "\nStatus: " + (data.status ? 'Active' : 'Inactive'));
                document.getElementById("designation_name").value = data.designation_name;  // Change 'department_name' to 'designation_name'
                document.getElementById("designation_code").value = data.designation_code;  // Change 'department_code' to 'designation_code'
                document.getElementById("status").value = data.status;
                console.log(data.status);
                $("#modal_basic").show();  // Assuming 'modal_basic' is the correct ID for your modal
                document.getElementById('spinner' + id).className = "fa fa-pencil";
            },
    
            error: function (error) {
                // Handle errors
                console.log(error);
            }
        });
    }
    
    function edit_divsrow(id) {
        document.getElementById('spinner' + id).className = "fa fa-spinner";
        document.getElementById("division_id").value = id;  // Change 'designation_id' to 'division_id'
    
        $.ajax({
            type: "GET",
            url: document.getElementById("url_name").value,
    
            data: {
                'id': id
            },
    
            dataType: "json",
            success: function (data) {
                // Handle the successful response
                // alert(data.message + "\nDivision Name: " + data.division_name +
                //       "\nStatus: " + (data.status ? 'Active' : 'Inactive'));
                document.getElementById("division_name").value = data.division_name;  // Change 'designation_name' to 'division_name'
                document.getElementById("status").value = data.status;
                console.log(data.status);
                $("#modal_basic").show();  // Assuming 'modal_basic' is the correct ID for your modal
                document.getElementById('spinner'+ id).className = "fa fa-pencil";
            },
    
            error: function (error) {
                // Handle errors
                console.log(error);
            }
        });
    }
    function edit_qualification_row(id) {
        document.getElementById('spinner' + id).className = "fa fa-spinner";
        document.getElementById("qualification_id").value = id;
    
        $.ajax({
            type: "GET",
            url: document.getElementById("url_name").value,
            data: {
                'id': id
            },
            dataType: "json",
            success: function (data) {
                document.getElementById("qualification_name").value = data.qualification_name;
                // Remove the following line since there's no qualification code
                // document.getElementById("qualification_code").value = data.qualification_code;
                document.getElementById("status").value = data.status;
                console.log(data.status);
                $("#modal_basic").show();
                document.getElementById('spinner' + id).className = "fa fa-pencil";
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
    
    function edit_class_row(id) {
        document.getElementById('spinner' + id).className = "fa fa-spinner";
        document.getElementById("class_id").value = id;
    
        $.ajax({
            type: "GET",
            url: document.getElementById("url_name").value,
            data: {
                'id': id
            },
            dataType: "json",
            success: function (data) {
                document.getElementById("class_name").value = data.class_name;
                // Remove the following line since there's no class code
                // document.getElementById("class_code").value = data.class_code;
                document.getElementById("status").value = data.status;
                console.log(data.status);
                $("#modal_basic").show();
                document.getElementById('spinner' + id).className = "fa fa-pencil";
            },
            error: function (error) {
                console.log(error);
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
                        // Handle success (e.g., department refresh the page or update the UI)
                    
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
    function delete_desrow1(id) {
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
    function delete_divsrow1(id) {
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
    
    function delete_qualification_row(id) {
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
    function delete_class_row(id) {
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
    
    
    function update_row() {
        // Department
        var id = document.getElementById("department_id").value;
        var department_name = document.getElementById("department_name").value;
        var department_code = document.getElementById("department_code").value;
        var status = document.getElementById("status").value;
    
        // Show loading indicator
        $("#loading_indicator").show();
    
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
                // Hide loading indicator on   departmeantsuccess
                $("#loading_indicator").hide();
    
                if (data.success !== '') {
                    alert(data.success);
                    $("#modal_basic").modal("hide");
                    window.location.reload(true);
                } else {
                    alert(data.error);
                }
            },
            error: function (error) {
                // Hide loading indicator on error
                $("#loading_indicator").hide();
    
                console.error('error occurred:', error);
            }
        });
    }
    function update_desrow() {
        // Designation
        var id = document.getElementById("designation_id").value;
        var designation_name = document.getElementById("designation_name").value;
        var designation_code = document.getElementById("designation_code").value;
        var status = document.getElementById("status").value;
    
        // Show loading indicator
        $("#loading_indicator").show();
    
        $.ajax({
            type: "GET",
            url: document.getElementById("url_update").value,
            data: {
                'id': id,
                'designation_name': designation_name,  // Change 'department_name' to 'designation_name'
                'designation_code': designation_code,  // Change 'department_code' to 'designation_code'
                'status': status
            },
            dataType: "json",
            success: function (data) {
                // Hide loading indicator on success
                $("#loading_indicator").hide();
    
                if (data.success !== '') {
                    alert(data.success);
                    $("#modal_basic").modal("hide");
                    window.location.reload(true);
                } else {
                    alert(data.error);
                }
            },
            error: function (error) {
                // Hide loading indicator on error
                $("#loading_indicator").hide();
    
                console.error('error occurred:', error);
            }
        });
    }
    function update_divsrow() {
        var id = document.getElementById("division_id").value;  // Change 'designation_id' to 'division_id'
        var division_name = document.getElementById("division_name").value;  // Change 'designation_name' to 'division_name'
        var status = document.getElementById("status").value;
        
        // Show loading indicator
        $("#loading_indicator").show();
        
        $.ajax({
            type: "GET",
            url: document.getElementById("url_update").value,
            data: {
                'id': id,
                'division_name': division_name,  // Change 'designation_name' to 'division_name'
                'status': status
            },
            dataType: "json",
            success: function (data) {
                // Hide loading indicator on success
                $("#loading_indicator").hide();
        
                if (data.success !== '') {
                    alert(data.success);
                    $("#modal_basic").modal("hide");
                    window.location.reload(true);
                } else {
                    alert(data.error);
                }
            },
            error: function (error) {
                // Hide loading indicator on error
                $("#loading_indicator").hide();
        
                console.error('error occurred:', error);
            }
        });
    }
    function update_qualification_row() {
        var id = document.getElementById("qualification_id").value;  // Change 'division_id' to 'qualification_id'
        var qualification_name = document.getElementById("qualification_name").value;  // Change 'division_name' to 'qualification_name'
        var status = document.getElementById("status").value;
        
        // Show loading indicator
        $("#loading_indicator").show();
        
        $.ajax({
            type: "GET",
            url: document.getElementById("url_update").value,
            data: {
                'id': id,
                'qualification_name': qualification_name,  // Change 'division_name' to 'qualification_name'
                'status': status
            },
            dataType: "json",
            success: function (data) {
                // Hide loading indicator on success
                $("#loading_indicator").hide();
    
                if (data.success !== '') {
                    alert(data.success);
                    $("#modal_basic").modal("hide");
                    window.location.reload(true);
                } else {
                    alert(data.error);
                }
            },
            error: function (error) {
                // Hide loading indicator on error
                $("#loading_indicator").hide();
    
                console.error('error occurred:', error);
            }
        });
    }
    function update_class_row() {
        var id = document.getElementById("class_id").value;  // Change 'qualification_id' to 'class_id'
        var class_name = document.getElementById("class_name").value;  // Change 'qualification_name' to 'class_name'
        var status = document.getElementById("status").value;
        
        // Show loading indicator
        $("#loading_indicator").show();
        
        $.ajax({
            type: "GET",
            url: document.getElementById("url_update").value,
            data: {
                'id': id,
                'class_name': class_name,  // Change 'qualification_name' to 'class_name'
                'status': status
            },
            dataType: "json",
            success: function (data) {
                // Hide loading indicator on success
                $("#loading_indicator").hide();
    
                if (data.success !== '') {
                    alert(data.success);
                    $("#modal_basic").modal("hide");
                    window.location.reload(true);
                } else {
                    alert(data.error);
                }
            },
            error: function (error) {
                // Hide loading indicator on error
                $("#loading_indicator").hide();
    
                console.error('error occurred:', error);
            }
        });
    }
    