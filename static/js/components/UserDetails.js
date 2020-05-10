import React, { Component } from 'react'
import UserPic from './UserPic'
import UserName from './UserName'
import CardTimeInfo from './CardTImeInfo'

class UserDetails extends Component {


    render() {
        return (
            <div className='row'>
                <div className='col-sm-1'>
                    <UserPic profPic='/static/img/profile_pics/default.png' />
                </div>
                <div className='col-sm-11'>
                    <UserName />
                    <CardTimeInfo />
                </div>
            </div>
        )
    }
}

export default UserDetails