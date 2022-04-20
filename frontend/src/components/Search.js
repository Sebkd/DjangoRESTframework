import React from 'react'

import {Space} from 'antd';
import {SearchOutlined} from '@ant-design/icons';


const SearchBar = ({onChange, placeholder}) => {
    return (
        <div className="Search">
      <span className="SearchSpan">
      <Space>
        <SearchOutlined/>
      </Space>
      </span>
            <input
                type="text"
                placeholder="Search"

                // value={searchTerm}
                // onChange={handleChange}
            />
            <ul>

                <li>{}</li>

            </ul>
            {/*<ul>*/}
            {/*    {searchResults.map(item => (*/}
            {/*        <li>{item}</li>*/}
            {/*    ))}*/}
            {/*</ul>*/}
            {/*<input*/}
            {/*    className="SearchInput"*/}
            {/*    type="text"*/}
            {/*    onChange={onChange}*/}
            {/*    placeholder={placeholder}*/}
            {/*/>*/}
        </div>
    );
};


export default SearchBar;
