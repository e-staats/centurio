import React, { Component } from 'react'

class Button extends Component {
    render() {
        return (
            <button type='button' className={this.props.buttonClass} onClick={this.props.clickHandler}>{this.props.buttonText}</button>
        )
    }
}

class CompleteButton extends Component {
    clickHandler() {
        console.log("You clicked! How can you click!")
    }
    
    render () {
        return (
            <Button buttonText="Complete" clickHandler={this.clickHandler} buttonClass='btn btn-outline-success btn-sm align-self-end'/>
        )
    }
}

class CommentButton extends Component {
    clickHandler() {
        console.log("You tried to comment")
    }

    render() {
        return (
            <Button buttonText="Comment" clickHandler={this.clickHandler} buttonClass='btn btn-outline-info btn-sm align-self-end'/>
        )
    }
}

export {
    CompleteButton,
    CommentButton,
}