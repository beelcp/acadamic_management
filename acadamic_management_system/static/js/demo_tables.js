
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
    function edit_employee_category_row(id) {
        document.getElementById('spinner' + id).className = "fa fa-spinner";
        document.getElementById("category_id").value = id;
    
        $.ajax({
            type: "GET",
            url: document.getElementById("url_name").value, // Change to your actual URL
            data: {
                'id': id
            },
            dataType: "json",
            success: function (data) {
                document.getElementById("category_name").value = data.employee_category_name;
                document.getElementById("category_area").value = data.employee_category_area;
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
    
function edit_subject_row(id) {
    document.getElementById('spinner' + id).className = "fa fa-spinner";
    document.getElementById("subject_id").value = id;

    $.ajax({
        type: "GET",
        url: document.getElementById("url_name").value,
        data: {
            'id': id
        },
        dataType: "json",
        success: function (data) {
            document.getElementById("subject_name").value = data.subject_name;
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
    
        box.find(".mb-control-yes").off("click").on("click", function () {
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
    
        box.find(".mb-control-yes").off("click").on("click", function () {
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
    
        box.find(".mb-control-yes").off("click").on("click", function () {
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
    
        box.find(".mb-control-yes").off("click").on("click", function () {
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
    function delete_employee_category_row(id) {
        var box = $("#mb-remove-row");
        box.addClass("open");
    
        box.find(".mb-control-yes").off("click").on("click", function () {
            box.removeClass("open");
    
            // Assuming you're using AJAX to send a GET request to the Django view
            $.ajax({
                type: "GET",
                url: document.getElementById("url_delete").value, // Change to your actual URL
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
    
        box.find(".mb-control-yes").off("click").on("click", function () {
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
    
function delete_subject_row(id) {
    var box = $("#mb-remove-row");
    box.addClass("open");

    box.find(".mb-control-yes").off("click").on("click", function () {
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
    

function update_employee_category_row() {
    var id = document.getElementById("category_id").value;
    var category_name = document.getElementById("category_name").value;
    var category_area = document.getElementById("category_area").value;
    var status = document.getElementById("status").value;
    
    // Show loading indicator
    $("#loading_indicator").show();
    
    $.ajax({
        type: "GET",
        url: document.getElementById("url_update").value,
        data: {
            'id': id,
            'category_name': category_name,
            'category_area': category_area,  // Include category area in the data sent to the server
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

            console.error('Error occurred:', error);
        }
    });
}

function update_subject_row() {
    var id = document.getElementById("subject_id").value;
    var subject_name = document.getElementById("subject_name").value;
    var status = document.getElementById("status").value;
    var class_name = document.getElementById("class_name").value;

    // Show loading indicator
    $("#loading_indicator").show();

    $.ajax({
        type: "GET",
        url: document.getElementById("url_update").value,
        data: {
            'id': id,
            'subject_name': subject_name,
            // 'subject_area': subject_area,  // Include subject area in the data sent to the server
            'status': status,
            'class_name':class_name
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

            console.error('Error occurred:', error);
        }
    });
}
function checkAll() {
    var selectAllCheckbox = document.getElementById("selectAllCheckbox");
    var classCheckboxes = document.querySelectorAll('.classCheckbox');
    
 classCheckboxes.forEach(function (checkbox) {

    checkbox.checked = selectAllCheckbox.checked;
});
}


function drop() {
    var employee_category = document.getElementById("employee_category_id").value;
    var drop = document.getElementById('drop');
    var arr=employee_category.split("+");
    //alert(arr[0]);
    if (arr[1]=== '2') {
        drop.style.display = "block";
    } else {
        drop.style.display = "none";
    }
}








function addRow() {
    var classId = document.getElementById("class").value;
    var className = document.getElementById("class").options[document.getElementById("class").selectedIndex].text;
    var divisionId = document.getElementById("division").value;
    var divisionName = document.getElementById("division").options[document.getElementById("division").selectedIndex].text;
    var subjectId = document.getElementById("subject").value;
    var subjectName = document.getElementById("subject").options[document.getElementById("subject").selectedIndex].text;

    var table = document.getElementById("dataTables").getElementsByTagName('tbody')[0];
    for (var i = 0, row; row = table.rows[i]; i++) {
        if (
            row.cells[0].innerHTML === className &&
            row.cells[1].innerHTML === divisionName &&
            row.cells[2].innerHTML === subjectName
        ) {

            // alert("This class, division, and subject combination already exists in the table.");
            noty({ text: 'This combination already exists in the table.', layout: 'topRight',timeout: 2000 ,type:'error' });
            return;
        }
    }

    // If no similar row found, add the new row
    var newRow = table.insertRow(table.rows.length);
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);

    var classIdInput = document.createElement("input");
    classIdInput.type = "hidden";
    classIdInput.name = "class_ids[]";  // Use array notation for multiple values
    classIdInput.value = classId;

    var divisionIdInput = document.createElement("input");
    divisionIdInput.type = "hidden";
    divisionIdInput.name = "division_ids[]";
    divisionIdInput.value = divisionId;

    var subjectIdInput = document.createElement("input");
    subjectIdInput.type = "hidden";
    subjectIdInput.name = "subject_ids[]";
    subjectIdInput.value = subjectId;



    cell1.innerHTML = className;
    cell2.innerHTML = divisionName;
    cell3.innerHTML = subjectName;
    cell4.innerHTML =  '<button class="btn btn-danger" onclick="deleteRow(this)"><span class="glyphicon glyphicon-trash"></span></button>';

    newRow.appendChild(classIdInput);
    newRow.appendChild(divisionIdInput);
    newRow.appendChild(subjectIdInput);
}


function deleteRow(btn) {
    var row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

// Make an AJAX request to fetch subjects for the selected class
// $.ajax({
//     type: 'GET',
//     url: document.getElementById("url_sub").value,
//     data: { 'class_id': selectedClass },
//     dataType: 'json',
//     success: function(data) {
//         // Add subjects based on the response
//         for (var i = 0; i < data.length; i++) {
//             var option = document.createElement('option');
//             option.value = data[i].id;
//             option.text = data[i].subject_name;
//             subjectsDropdown.appendChild(option);
//         }
//     },
//     error: function(error) {
//         console.error('Error occurred:', error);
//     }
// });









function updateSubjects() {
    var classId = document.getElementById("class").value;
    var subjectDropdown = document.getElementById("subject");
    console.log(classId);
    var request_url = document.getElementById('url_sub').value;
    subjectDropdown.innerHTML = '';

    // Fetch subjects based on the selected class using AJAX
    $.ajax({
        url: request_url,
        type: 'GET',
        data: { "classId": classId },
        dataType: 'json',
        success: function (data) {
            data.subjects.forEach(function (item) {
                var option = document.createElement("option");
                option.value = item.id;
                option.text = item.subject_name;
                subjectDropdown.add(option);
            });
        },
        error: function (error) {
            console.log('Error fetching subjects:', error);
        }
    });
}


function showQrCode(imageUrl) {
  $('#qrCodeImage').attr('src', imageUrl);
  $('#qrCodeModal').modal('show');
}

