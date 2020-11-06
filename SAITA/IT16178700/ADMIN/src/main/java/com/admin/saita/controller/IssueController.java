package com.admin.saita.controller;

import com.admin.saita.dto.IssueDTO;
import com.admin.saita.service.IIssueService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Created by KaushiRajapakshe on 4/11/2020.
 */

/**
 * Issue Controller for insert,
 * get issue{id}, get all issue
 */
@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/react/feedback")
public class IssueController {

    //    Create final variable for logger
    private static final Logger LOGGER = LoggerFactory.getLogger(IssueController.class);

    //    Issue service interface object
    @Autowired
    private IIssueService issueService;

    //    Get all User feedback
    @GetMapping(value = "/issue")
    public @ResponseBody ResponseEntity<List<IssueDTO>> getIssueFeedback() {
        List<IssueDTO> result = issueService.getAllIssueFeedback();
        LOGGER.info("Get issue {}", result);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    //    Add user feedback
    @PostMapping(value = "/issue")
    public ResponseEntity<IssueDTO> insertIssue(@RequestBody IssueDTO issue) {
        IssueDTO result = issueService.insertIssueFeedback(issue);
        LOGGER.info("Insert issue {}", result);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    //    Update user feedback
    @PatchMapping(value = "/issue/{id}")
    public @ResponseBody ResponseEntity<IssueDTO> updateIssue(@PathVariable(value="id")int id, @RequestBody IssueDTO issue) {
        IssueDTO result = issueService.updateIssueFeedback(id, issue);
        LOGGER.info("Get issue by id {} {}", id, result);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }

    //    Delete user feedback
    @DeleteMapping(value = "/issue/{id}")
    public @ResponseBody ResponseEntity<String> deleteFeedback(@PathVariable(value="id")int id) {
        String result = issueService.deleteIssueFeedback(id);
        LOGGER.info("Delete issue {}", id, result);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }


}
