import {Button, Form, Input, InputNumber} from "antd";
import React from "react";
// import "antd/dist/antd.css";
// import "./index.css";


const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

class GenreForm extends React.Component {
    constructor(props) {
        super(props);
        this.genreInfo = {};
        this.fin = this.onFinish.bind(this);
    }

    render(){
        return (
            <Form {...layout} name="nest-messages" onFinish={ this.fin }>
                <Form.Item name={['name']} label="Name" rules={[{ required: true }]}>
                    <Input />
                </Form.Item>
                <Form.Item name={['email']} label="Email" rules={[{ type: 'email' }]}>
                </Form.Item>
                <Form.Item name={['age']} label="Age" rules={[{ type: 'number', min: 0, max: 99 }]}>
                    <InputNumber />
                </Form.Item>
                <Form.Item name={['user', 'website']} label="Website">
                    <Input />
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        Submit
                    </Button>
                </Form.Item>
      </Form>
        );
    };

    onFinish = (values)=>{
        return values;
    };

    sendInfo = ()=>{
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this.userInfo)
        };
        fetch('http://127.0.0.1:5000/user_info', requestOptions)
            .then(function(response) {
                const res = response.json();
                console.log(res);
            });
    };
    getRecommendation = ()=>{
        // let req = new Request(" http://127.0.0.1:5000/");
        // fetch(req, {method:'OPTIONS'}).then(function(response){console.log(response)});
        // fetch(req, {method:'GET'}).then(function(response){console.log(response)});
    };
}

export default GenreForm;