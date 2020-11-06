package com.admin.saita.dto;

import com.fasterxml.jackson.annotation.JsonInclude;

import java.util.List;
/**
 * Created by KaushiRajapakshe on 4/11/2020.
 */

/**
 * Issue DTO for insert,
 * get issue attributes
 * and set issue attributes
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
public class IssueDTO {
    private int id;
    private String applicationName;
    private String applicationVersion;
    private String errorDescription;
    private String errorStatus;
    private String errorAction;
    private String errorTarget;
    private String userFirstName;
    private String userLastName;
    private String userEmail;
    private List<IssueDTO> children;

    public IssueDTO() {
        // create IssueDTO object
    }

    public String getUserFirstName() {
        return userFirstName;
    }

    public void setUserFirstName(String userFirstName) {
        this.userFirstName = userFirstName;
    }

    public String getUserLastName() {
        return userLastName;
    }

    public void setUserLastName(String userLastName) {
        this.userLastName = userLastName;
    }

    public String getUserEmail() {
        return userEmail;
    }

    public void setUserEmail(String userEmail) {
        this.userEmail = userEmail;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getApplicationName() {
        return applicationName;
    }

    public void setApplicationName(String applicationName) {
        this.applicationName = applicationName;
    }

    public String getApplicationVersion() {
        return applicationVersion;
    }

    public void setApplicationVersion(String applicationVersion) {
        this.applicationVersion = applicationVersion;
    }

    public String getErrorDescription() {
        return errorDescription;
    }

    public void setErrorDescription(String errorDescription) {
        this.errorDescription = errorDescription;
    }

    public String getErrorStatus() {
        return errorStatus;
    }

    public void setErrorStatus(String errorStatus) {
        this.errorStatus = errorStatus;
    }

    public String getErrorAction() {
        return errorAction;
    }

    public void setErrorAction(String errorAction) {
        this.errorAction = errorAction;
    }

    public String getErrorTarget() {
        return errorTarget;
    }

    public void setErrorTarget(String errorTarget) {
        this.errorTarget = errorTarget;
    }

    public List<IssueDTO> getChildren() {
        return children;
    }

    public void setChildren(List<IssueDTO> children) {
        this.children = children;
    }

}
