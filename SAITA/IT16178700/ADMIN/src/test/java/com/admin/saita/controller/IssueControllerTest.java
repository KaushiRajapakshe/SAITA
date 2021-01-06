package com.admin.saita.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.boot.test.context.SpringBootTest;
import com.admin.saita.dto.IssueDTO;

import static org.junit.Assert.*;

/**
 * Created by KaushiRajapakshe on 2/12/2020.
 */

/**
 * Issue Controller Test Cases
 */

@SpringBootTest
@RunWith(SpringRunner.class)
public class IssueControllerTest {
    @Autowired
    private IssueController issueController;

    @Test
    public void addIssueTest()  {
//        Create IssueDTO object
        IssueDTO issue = new IssueDTO();
        issue.setApplicationName("VSCode");
        issue.setContactNumber("777425432");
        issue.setApplicationVersion("2019.1.4");
        issue.setErrorType("Application");
        issue.setUserEmail("kaushi.rajapakshe1@gmail.com");
        issue.setUserName("Kaushi Rajapakshe");
        issue.setErrorDescription("9000 port block");

        IssueDTO aIssue = issue;
        aIssue.setId(0);

        ObjectMapper mapper = new ObjectMapper();
        String actualResult = null;
        try {
            actualResult = mapper.writeValueAsString(aIssue);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
//        Insert Issue function call
        String expectedResult = new Gson().toJson(issueController.insertIssue(issue).getBody(), new TypeToken<Object>() {
        }.getType());

//        Check actual and expected values
        assertEquals(actualResult,expectedResult);
    }

    @Test
    public void deleteIssueTest() {
        // Delete Issue function call
        String expectedResult = issueController.deleteFeedback(100).getBody();
        String actualResult = "Delete Fail for feedback id : 100";

        // Check actual and expected values
        assertEquals(actualResult,expectedResult);
    }

    @Test
    public void deleteIssuesTest() {
        // Delete Issue function call
        String expectedResult = issueController.deleteFeedback(150).getBody();
        String actualResult = "Delete Fail for feedback id : 150";

        // Check actual and expected values
        assertEquals(actualResult,expectedResult);
    }
}