package com.admin.saita.service;

import com.admin.saita.dto.IssueDTO;

import java.util.List;
/**
 * Created by KaushiRajapakshe on 4/11/2020.
 */

/**
 * Issue IIssueService Interface
 */

public interface IIssueService {

    List<IssueDTO> getAllIssueFeedback();
    IssueDTO insertIssueFeedback(IssueDTO issue);
    IssueDTO updateIssueFeedback(int id, IssueDTO issue);
    String deleteIssueFeedback(int issue);
}
