import {Button, Form, Input, InputNumber, Select, Checkbox} from "antd";
import React from "react";
import "antd/dist/antd.css";

const layout = {
    labelCol: {
        span: 8,
    },
    wrapperCol: {
        span: 16,
    },
};

const genreOptions = [
    { label: 'Blues', value: 2 },
    { label: 'Classical', value: 4 },
    { label: 'Country', value: 8 },
    { label: 'Easy Listening', value: 12 },
    { label: 'Electronic', value: 14 },
    { label: 'Experimental', value: 31 },
    { label: 'Folk', value: 16 },
    { label: 'Hip-Hop', value: 20 },
    { label: 'Instrumental', value: 162 },
    { label: 'International', value: 1 },
    { label: 'Jazz', value: 3 },
    { label: 'Old-Time / Historic', value: 7 },
    { label: 'Pop', value: 9 },
    { label: 'Rock', value: 11 },
    { label: 'Soul-RnB', value: 13 },
    { label: 'Spoken', value: 19 }
];

class UserForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {music_id: -1};
        this.handleSend = this.sendInfo.bind(this);
    }

    render(){
        return (
            <div>
                <div>
                    <p>First, let as ask you some questions about you: </p>
                </div>
                <Form {...layout} name="nest-messages" onFinish={ this.onFinish }>
                    <div>
                        <Form.Item name={['name']} label="Name" required={true}>
                            <Input />
                        </Form.Item>
                        <Form.Item name={['age']} label="Age" rules={[{ type: 'number', min: 0, max: 99 }]} required={true}>
                            <InputNumber />
                        </Form.Item>
                        <Form.Item
                            name={['gender']}
                            label="Gender"
                            required={true}
                            rules={[
                                {required: true,},
                            ]}>
                            <Select>
                                <Select value="male">Male</Select>
                                <Select value="female">Female</Select>
                            </Select>
                        </Form.Item>
                        <Form.Item name={['genres']} label="Some genres you might be interested in:">
                            <Checkbox.Group options={genreOptions} />
                        </Form.Item>
                        <Form.Item>
                            <Button {...layout.wrapperCol}
                                    type="primary"
                                    htmlType="submit">
                                Submit
                            </Button>
                        </Form.Item>
                    </div>
                </Form>
            </div>
        )
    }
    sendInfo = (values)=>{
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(values)
        };
        fetch('http://127.0.0.1:5000/getresult', requestOptions)
            .then(response =>  response.json())
            .then((data) => {this.props.history.push(
                {pathname: '/results',
                    state: { detail: data }})});
    }

     onFinish = (values)=>{
        this.sendInfo(values);
    }
}

export default UserForm;