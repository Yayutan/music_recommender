import React, { Component } from "react";
import {Link} from "react-router-dom";

class Main extends Component {
  render() {
    return (
            <div>
            <h1>Music Recommender</h1>
            <ul className="header">
              <p>Welcome to the Music Recommender site!</p>
              <p>Put in some information about yourself and we will find music you might like!</p>
          </ul>
                <Link to="/userinfo">
                    <button type="button">
                        Get Started
                    </button>
                </Link>
        </div>
    );
  }
}

export default Main;