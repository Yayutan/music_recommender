import React, { Component } from "react";
import {Button, Row, Col} from "antd";
import ReactAudioPlayer from 'react-audio-player';
import {Link} from "react-router-dom";
import "./App.css"

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

const music_base_url = "http://localhost:5000/static/";
class BasicResults extends Component {
    handleClick(){
    // TODO: need to record log to backend
    this.props.history.push('/');
  };

  render() {
      const musicPath = this.props.location.state.detail;
      console.log(musicPath);
    return (
        <>
          <h3>How do you like the music?</h3>
          <Row>
            <Col span={8}>
              <ReactAudioPlayer
                  src= {music_base_url + musicPath.path0}
                  controls
              />
            </Col>
            <Col span={8}>
              <ReactAudioPlayer
                  src= {music_base_url + musicPath.path1}
                  controls
              />
            </Col>
            <Col span={8}>
              <ReactAudioPlayer
                  src= {music_base_url + musicPath.path2}
                  controls
              />
            </Col>
          </Row>
           <Row>
            <Col span={8}>
              <Button>
                Music 1
              </Button>
            </Col>
            <Col span={8}>
              <Button>
                Music 2
              </Button>
            </Col>
            <Col span={8}>
              <Button>
                Music 3
              </Button>
            </Col>
          </Row>
          <Row>
            <Col span={8}></Col>
            <Col span={8}>
              <Link to="/">
                <Button>
                Try Again
              </Button>
              </Link>
            </Col>
            <Col span={8}></Col>
          </Row>
        </>
    );
  }
}

export default BasicResults;