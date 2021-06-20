import React, { Component } from "react";
import {HashRouter, Route} from "react-router-dom";
import UserForm from "./UserForm";
import BasicResults from "./BasicRecommendResult";
import Home from "./Home";

class Main extends Component {
    render() {
        return (
            <HashRouter>
                <div>
                    <div className="content">
                        <Route exact path="/" component={Home}/>
                        <Route path="/userinfo" component={UserForm}/>
                        <Route path="/results" component={BasicResults}/>
                    </div>
                </div>
            </HashRouter>
        );
    }
}

export default Main;