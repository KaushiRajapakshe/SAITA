import React from 'react';
import './App.css';

import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import image from './image/SAITA.png';

import Feedback from "./Feedback.js";
import Home from "./Home.js";

// React Header function
function Header() {

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

    // returning react header ui view component
    return (
        <Router>
            <AppBar position="static">
                <Toolbar className="toolbar">
                    <Typography>
                        <img src={image} className={classes.navIcon} />
                    </Typography>
                    <Typography variant="h6" className={classes.title}>
                        SAITA Feedback UI
          </Typography>
                    <Button component={Link} to='/' color="inherit" className={classes.navButton}>Home</Button>
                    <Button component={Link} to='/feedback' color="inherit" className={classes.navButton}>User Feedback</Button>
                </Toolbar>
            </AppBar>
            {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
            <Switch>
                <Route path="/feedback">
                    <Feedback />
                </Route>
                <Route path="/">
                    <Home />
                </Route>
            </Switch>
        </Router>
    );

}

export default Header;