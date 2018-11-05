import React, { Component } from 'react'

import {Editor} from 'slate-react';
import {Value} from 'slate';

import DropzoneComponent from 'react-dropzone-component';

const initialValue = Value.fromJSON({
    document: {
        nodes: [
          {
            object: 'block',
            type: 'paragraph',
            nodes: [
              {
                object: 'text',
                leaves: [
                  {
                    text: 'A line of text in a paragraph.',
                  },
                ],
              },
            ],
          },
        ],
    },
});



export default class QuestionTopbar extends Component {

    constructor(props) {
        super(props);
        this.djsConfig = {
            addRemoveLinks: true,
            acceptedFiles: "image/jpeg,image/png,image/gif",
            autoProcessQueue: false
        };

        this.componentConfig = {
            iconFiletypes: ['.jpg', '.png', '.gif'],
            showFiletypeIcon: true,
            postUrl: 'no-url'
        };



    }
    state = {
        value: initialValue
    }


    onChange = ({value}) => {
        this.setState({
            value
        });
    }

    handleFileAdded(file) {
        console.log(file);
    }
    
  render() {
    const config = this.componentConfig;
    const djsConfig = this.djsConfig;
        // For a list of all possible events (there are many), see README.md!
    const eventHandlers = {
        addedfile: this.handleFileAdded.bind(this)
    }
    
    return (
      <React.Fragment>
            <div className="post-topbar">
                <div className="user-picy">
                    <img src="/images/resources/user-pic.png" />
                </div>
                <div className="post-st">
                    <div className = "post-content">
                        <Editor 
                            value = {this.state.value}
                            onChange = {this.onChange}
                        />
                    </div>
                    <div className = "post-img">
                        <DropzoneComponent config={config}
                        eventHandlers={eventHandlers}
                        djsConfig={djsConfig} />
                    </div>
                    <ul>
                        <li><a className="post-jb active" href="#" >Post this question</a></li>
                    </ul>
                </div>{/*post-st end*/}
            </div>{/*post-topbar end*/}
      </React.Fragment>
    )
  }
}
