package com.admin.saita.service.implementation;

import com.admin.saita.dto.IssueDTO;
import com.admin.saita.repository.IssueDAO;
import com.admin.saita.service.IIssueService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

/**
 * Created by KaushiRajapakshe on 4/11/2020.
 */

/**
 * Issue Service for
 * implement service interface methods
 */
@Service
public class IssueService implements IIssueService {

    //    Create Issue DAO object
    @Autowired
    private IssueDAO issueDAO;

    //    Get all feedback function
    @Override
    public List<IssueDTO> getAllIssueFeedback() {
        List<IssueDTO> result = null;
        Optional<List<IssueDTO>> value = issueDAO.getAllFeedback();
        if (value.isPresent()) {
            result =  value.get();
        }
        return result;
    }

    //    Insert feedback function
    @Override
    public IssueDTO insertIssueFeedback(IssueDTO issue) {
        return issueDAO.insertUserFeedback(issue);
    }

    //    Update feedback function
    @Override
    public IssueDTO updateIssueFeedback(int id, IssueDTO issue) {
        return issueDAO.updateUserFeedback(id, issue);
    }

    //    Delete feedback function
    @Override
    public String deleteIssueFeedback(int id) {
        return issueDAO.deleteFeedbackIssueDetail(id);
    }
}
