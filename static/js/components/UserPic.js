import React, { Component } from 'react'

class UserPic extends Component {


    render() {
        return (
            <img className='prof-pic-small' src={this.props.profPic} alt='prof-pic'/>
        )
    }
}

export default UserPic