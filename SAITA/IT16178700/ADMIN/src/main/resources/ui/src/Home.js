// src/components/bootstrap-carousel.component.js
import React from "react";

import { Carousel } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

class Home extends React.Component {

    render() {
        return (
            <div className="home">
                <div className='container-fluid' >
                    <div className="row">
                        <div className="col-12">
                            <Carousel>
                                <Carousel.Item interval={500}>
                                    <img
                                        className="d-block w-100"
                                        src="../s2.jpg"
                                        alt="First slide"
                                    />
                                    <Carousel.Caption>
                                        <h1>Solve your issue with SAITA</h1>
                                        <p>You can fix your any windows issue with SAITA system.</p>
                                    </Carousel.Caption>
                                </Carousel.Item>
                                <Carousel.Item>
                                    <img
                                        className="d-block w-100"
                                        src="../s3.jpg"
                                        alt="Second slide"
                                    />
                                    <Carousel.Caption>
                                        <h1>Configure your windows with SAITA</h1>
                                        <p>Setup environments on windows using SAITA without any issue.</p>
                                    </Carousel.Caption>
                                </Carousel.Item>
                            </Carousel>
                        </div>
                    </div>
                </div>
                <div className="home-content">
                    <h2 className="home-title"><b>SMART ARTIFICIAL INTELLIGENT TROUBLESHOOTING AGENT</b></h2>
                    <p className="home-description">While working on computers, people frequently confront with various kinds of problems,
                    those beyond their extensive expertise. Microsoft Windows is the widely used Operating
                    System running on numerous personal computers (PCs) and the reason which gives more
                    irritating problems that require to be addressed. Currently, troubleshooting is considered
                    as a costly and time-consuming approach. The SAITA is an Artificial Intelligent
                    Troubleshooting Agent which is a machine learning based system for solving most common
                    Windows-specific issues within a short period of time than the traditional approach.
                    The assistant learns from the accessible data and accomplishes the task for PC users as
                    performed by human experts. The main objective of this exploration venture is to distinguish
                    the constraints of existing troubleshooting software and create an AI troubleshooting
                    assistant to provide solutions to fix the identified user issues. The use of this assistant
                    would be economical as an IT help desk alternative in the industry. SAITA is developed to
                    serve as a representative troubleshooter for fundamental user issues, service issues,
                    application issues, and perform environment setup by analyzing software. This system will be
                 able to solve the common Windows user’s issues as same as a human with less time.</p>
                </div>
            </div>
        )
    };
}

export default Home;