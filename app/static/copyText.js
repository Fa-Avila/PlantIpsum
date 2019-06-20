/* eslint-env browser */
/* global document */
document.querySelector('#copyButton').addEventListener('click', function(){
      var reference_element = document.querySelector('#result');
      var range = document.createRange();
      range.selectNodeContents(reference_element);
      window.getSelection().addRange(range);
      var success = document.execCommand('copy');
      if(success){
        /* eslint-disable no-console */
        console.log('Success');
        /* eslint-enable no-console */
      }
      else{
        /* eslint-disable no-console */
        console.log('fail');
        /* eslint-enable no-console */
      }
      window.getSelection().removeRange(range);
    });