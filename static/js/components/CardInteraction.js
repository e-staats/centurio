import React, { Component } from 'react'
import { CompleteButton, CommentButton } from './Buttons.js'

class CardInteraction extends Component {
    render() {
        return (
            <div className="row">
                <div className="col-md-12 text-right">
                    <CommentButton />
                    <CompleteButton />
                </div>
            </div>
        )
    }
}

export default CardInteraction