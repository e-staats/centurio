import React, { Component } from 'react'
import CardInteraction from './CardInteraction'
import UserDetails from './UserDetails'
import CardInfo from './CardInfo'
import CardDayDetails from './CardDayDetail'
import CardDayComment from './CardDayComment'

class FeedCard extends Component {
    

    render () {
        return(
            <div className="feed-card">
                <UserDetails />
                <CardInfo />
                <CardDayDetails />
                <CardDayComment />
                <CardInteraction />
            </div>
        )
    }
}

export default FeedCard