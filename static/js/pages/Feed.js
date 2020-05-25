import React, { Component } from 'react'
import FeedCard from '../components/FeedCard'
import InfiniteScroll from 'react-infinite-scroll-component'

class Feed extends Component {
  state = {
    cards: [],
    initialCount: 20,
    moreCount: 10,
  };

  componentDidMount() {
    this.fetchData(this.state.initialCount)
  }

  fetchMoreData = () => {
    this.fetchData(this.state.moreCount)
  };

  fetchData = (count) => {
    var arr = []
    for (var i = 0; i < count; i++) {
      arr.push(i)
    }
    this.setState({ cards: this.state.cards.concat(arr) })
  };

  render() {
    return (
      <div>
        <hr />
        <div className='main-feed'>
          <InfiniteScroll
            dataLength={this.state.cards.length}
            next={this.fetchMoreData}
            hasMore={true}
            loader={<h4>Loading...</h4>}
          >
            {this.state.cards.map((cards, index) => (
              <FeedCard />
            ))}
          </InfiniteScroll>
        </div>
      </div>
    );
  }
}

ReactDOM.render(
  <Feed />,
  document.getElementById('feed')
)