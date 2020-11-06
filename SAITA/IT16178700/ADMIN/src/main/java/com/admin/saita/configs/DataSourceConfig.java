package com.admin.saita.configs;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

/**
 * Created by KaushiRajapakshe on 5/11/2020.
 */

/**
 * Data Source Configuration
 * for store mysql configuration
 */
@Configuration
public class DataSourceConfig {
    @Bean(name = "saita")
    @ConfigurationProperties(prefix = "db.saita")
    public DataSource dataSource1() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "jdbcTemplate")
    public JdbcTemplate jdbcTemplate(@Qualifier("saita") DataSource ds) {
        return new JdbcTemplate(ds);
    }
}
