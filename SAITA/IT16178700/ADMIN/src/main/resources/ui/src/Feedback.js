// Application related admin view main react ui
import React, { useState, useEffect } from 'react';
import './App.css';
import { forwardRef } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';

import MaterialTable from "material-table";
import AddBox from '@material-ui/icons/AddBox';
import ArrowDownward from '@material-ui/icons/ArrowDownward';
import Check from '@material-ui/icons/Check';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import Clear from '@material-ui/icons/Clear';
import DeleteOutline from '@material-ui/icons/DeleteOutline';
import Edit from '@material-ui/icons/Edit';
import FilterList from '@material-ui/icons/FilterList';
import FirstPage from '@material-ui/icons/FirstPage';
import LastPage from '@material-ui/icons/LastPage';
import Remove from '@material-ui/icons/Remove';
import SaveAlt from '@material-ui/icons/SaveAlt';
import Search from '@material-ui/icons/Search';
import ViewColumn from '@material-ui/icons/ViewColumn';
import axios from 'axios'
import Alert from '@material-ui/lab/Alert';
import { makeStyles } from '@material-ui/core/styles';

// Table icon set
const tableIcons = {
    Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
    Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
    Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
    DetailPanel: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
    Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
    Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
    FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
    LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
    NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
    PreviousPage: forwardRef((props, ref) => <ChevronLeft {...props} ref={ref} />),
    ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
    Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
    SortArrow: forwardRef((props, ref) => <ArrowDownward {...props} ref={ref} />),
    ThirdStateCheck: forwardRef((props, ref) => <Remove {...props} ref={ref} />),
    ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />)
};

// Application realted admin view react api base url
const api = axios.create({
    baseURL: `http://localhost:8083/api/react/feedback`
})

// validate email
function validateEmail(email) {
    const re = /^((?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]))$/;
    return re.test(String(email).toLowerCase());
}

// React Feedback function
function Feedback() {
    var columns = [
        { title: "id", field: "id", hidden: true },
        { title: "Error Type", field: "errorType" },
        { title: "Error Description", field: "errorDescription" },
        { title: "User name", field: "userName" },
        { title: "Contact Number", field: "contactNumber" },
        { title: "User Email", field: "userEmail" },
        { title: "Application Name", field: "applicationName" },
        { title: "Application Version", field: "applicationVersion" }
    ]
    const [data, setData] = useState([]); //table data

    //for error handling
    const [iserror, setIserror] = useState(false)
    const [errorMessages, setErrorMessages] = useState([])

    // Get user issue feedback
    useEffect(() => {
        api.get("/issue")
            .then(res => {
                setData(res.data)
            })
            .catch(error => {
                console.log("Error")
            })
    }, [])

    // Upadte user feedback
    const handleRowUpdate = (newData, oldData, resolve) => {
        //validation
        let errorList = []
        if (newData.errorType === "") {
            errorList.push("Please enter error type")
        }
        if (newData.applicationName === "") {
            errorList.push("Please enter application name")
        }
        if (newData.applicationVersion === "") {
            errorList.push("Please enter application version")
        }
        if (newData.errorDescription === "") {
            errorList.push("Please enter error description")
        }
        if (newData.userName === "") {
            errorList.push("Please enter user name")
        }
        if (newData.contactNumber === "") {
            errorList.push("Please enter contact number")
        }
        if (newData.userEmail === "" || validateEmail(newData.userEmail) === false) {
            errorList.push("Please enter a valid email")
        }

        if (errorList.length < 1) {
            api.patch("/issue/" + newData.id, newData)
                .then(res => {
                    const dataUpdate = [...data];
                    const index = oldData.tableData.id;
                    dataUpdate[index] = newData;
                    setData([...dataUpdate]);
                    resolve()
                    setIserror(false)
                    setErrorMessages([])
                })
                .catch(error => {
                    setErrorMessages(["Update failed! Server error"])
                    setIserror(true)
                    resolve()

                })
        } else {
            setErrorMessages(errorList)
            setIserror(true)
            resolve()

        }

    }

    // Added new user feedback from admin side
    const handleRowAdd = (newData, resolve) => {
        //validation
        let errorList = []
        if (newData.errorType === "") {
            errorList.push("Please enter error type")
        }
        if (newData.applicationName === "") {
            errorList.push("Please enter application name")
        }
        if (newData.applicationVersion === "") {
            errorList.push("Please enter application version")
        }
        if (newData.errorDescription === "") {
            errorList.push("Please enter error description")
        }
        if (newData.userName === "") {
            errorList.push("Please enter user name")
        }
        if (newData.contactNumber === "") {
            errorList.push("Please enter contact Nnumber")
        }
        if (newData.userEmail === "" || validateEmail(newData.userEmail) === false) {
            errorList.push("Please enter a valid email")
        }

        if (errorList.length < 1) { //no error
            api.post("/issue", newData)
                .then(res => {
                    let dataToAdd = [...data];
                    dataToAdd.push(newData);
                    setData(dataToAdd);
                    resolve()
                    setErrorMessages([])
                    setIserror(false)
                })
                .catch(error => {
                    setErrorMessages(["Cannot add data. Server error!"])
                    setIserror(true)
                    resolve()
                })
        } else {
            setErrorMessages(errorList)
            setIserror(true)
            resolve()
        }


    }

    // Delete unwanted user feedback
    const handleRowDelete = (oldData, resolve) => {

        api.delete("/issue/" + oldData.id)
            .then(res => {
                const dataDelete = [...data];
                const index = oldData.tableData.id;
                dataDelete.splice(index, 1);
                setData([...dataDelete]);
                resolve()
            })
            .catch(error => {
                setErrorMessages(["Delete failed! Server error"])
                setIserror(true)
                resolve()
            })
    }

    const useStyles = makeStyles((theme) => ({
        title: {
            marginRight: theme.spacing(2),
            color: "#ffc500!important",
            textAlign: 'left',
            flex: 1
        },
        navButton: {
            textAlign: 'right',
            alignSelf: 'stretch'
        },
        navIcon: {
            padding: '5px',
            width: '35px'
        }
    }));

    const classes = useStyles();

    // returning react ui view with user feedback table data
    return (
        <Router>
            <div className="feedback">
                <div>
                    {iserror &&
                        <Alert severity="error">
                            {errorMessages.map((msg, i) => {
                                return <div key={i}>{msg}</div>
                            })}
                        </Alert>
                    }
                </div>
                <MaterialTable
                    title="Application related user feedback "
                    columns={columns}
                    data={data}
                    icons={tableIcons}
                    editable={{
                        onRowUpdate: (newData, oldData) =>
                            new Promise((resolve) => {
                                handleRowUpdate(newData, oldData, resolve);

                            }),
                        onRowAdd: (newData) =>
                            new Promise((resolve) => {
                                handleRowAdd(newData, resolve)
                            }),
                        onRowDelete: (oldData) =>
                            new Promise((resolve) => {
                                handleRowDelete(oldData, resolve)
                            }),
                    }}
                />
            </div>
        </Router>
    );
}



export default Feedback;
