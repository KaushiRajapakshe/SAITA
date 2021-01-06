package com.admin.saita.repository;

import com.admin.saita.dto.IssueDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.PreparedStatementCreator;
import org.springframework.stereotype.Repository;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;
import java.util.Optional;

/**
 * Created by KaushiRajapakshe on 4/11/2020.
 */

/**
 * Issue DAO for insert,
 * get issue attributes
 * and set issue attributes on db
 */
@Repository
public class IssueDAO {

    //    Create jdbc object
    @Autowired
    private JdbcTemplate jdbcTemplate;

    //    Get all user feedback issues
    public Optional<List<IssueDTO>> getAllFeedback() {
        String sql = "SELECT * FROM feedback";
        List<IssueDTO> issue = jdbcTemplate.query(sql, new BeanPropertyRowMapper<>(IssueDTO.class));

        return Optional.of(issue);
    }

    //    Insert user feedback issue
    public IssueDTO insertUserFeedback(IssueDTO issue) {

        String sqlCheck = "SELECT COUNT(*) FROM `feedback` WHERE " +
                "applicationName='" + issue.getApplicationName() + "' AND " +
                "applicationVersion='" + issue.getApplicationVersion() + "' AND " +
                "errorType='" + issue.getErrorType() + "' AND " +
                "errorDescription='" + issue.getErrorDescription() + "'";
        Integer issueCount = jdbcTemplate.queryForObject(sqlCheck, Integer.class);
        if(issueCount >= 0){
            //    Insert SQL query
            String sql = "INSERT INTO `feedback` ( " +
                    "`applicationName`, " +
                    "`applicationVersion`, " +
                    "`errorType`, " +
                    "`errorDescription`, " +
                    "`userName`, " +
                    "`contactNumber`, " +
                    "`userEmail`) VALUES (?, ?, ?, ?, ?, ?, ?) ON DUPLICATE KEY UPDATE " +
                    "applicationName=values(applicationName), " +
                    "applicationVersion=values(applicationVersion), " +
                    "errorType=values(errorType), " +
                    "errorDescription=values(errorDescription)";

            jdbcTemplate.update(new PreparedStatementCreator() {
                @Override
                public PreparedStatement createPreparedStatement(Connection connection) throws SQLException {
                    PreparedStatement ps = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
                    ps.setString(1, issue.getApplicationName());
                    ps.setString(2, issue.getApplicationVersion());
                    ps.setString(3, issue.getErrorType());
                    ps.setString(4, issue.getErrorDescription());
                    ps.setString(5, issue.getUserName());
                    ps.setString(6, issue.getContactNumber());
                    ps.setString(7, issue.getUserEmail());
                    return ps;
                }
            });
        }


        //    return issue feedback
        return issue;
    }

    //    Update feedback issue
    public IssueDTO updateUserFeedback(int id, IssueDTO issue){
        //    Get user entered feedback id sql
        String sql = "UPDATE `feedback` SET " +
                "applicationName='" + issue.getApplicationName() +"', " +
                "applicationVersion='" + issue.getApplicationVersion() + "', " +
                "errorType='" + issue.getErrorType() + "', " +
                "errorDescription='" + issue.getErrorDescription() + "', " +
                "userName='" + issue.getUserName() + "', " +
                "contactNumber='" + issue.getContactNumber() + "', " +
                "userEmail='" + issue.getUserEmail() + "' " +
                "WHERE id=" + id + "";

        int result = jdbcTemplate.update(sql);
        if (result >0)
            return issue;
        return new IssueDTO();
    }

    //    Delete feedback issue
    public String deleteFeedbackIssueDetail(int id){
        //    Delete user entered feedback id sql
        String sql = "DELETE FROM `feedback` WHERE id='" + id + "'";
        int response = jdbcTemplate.update(sql);
        String msg;

        if (response == 1) {
            msg = "Delete Successful for feedback id : " + id;
        } else {
            msg = "Delete Fail for feedback id : " + id;
        }
        return msg;
    }

}
