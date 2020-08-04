<html>
	<head>
		<style type="text/css">
			.container {
				position: static;
				width: 800px;
				height: 350px;
				overflow: hidden;
			}
			.embed {
				height: 100%;
				width: 100%;
				min-width: 1000px;
				margin-left: -360px;
				margin-top: -57px;
				overflow: hidden;
			}
			body {
				width: 800px;
				margin: auto;
				padding: 1em;
				font-family: "Open Sans", sans-serif;
				line-height: 150%;
				letter-spacing: 0.1pt;
			}
			img {
				width: 90%;
				text-align: center;
				margin: auto;
				box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			}
			pre, code {
				padding: 1em;
			}
		</style>
		<script>
			document.addEventListener('readystatechange', event => {
				if (event.target.readyState === "complete")
					document.activeElement.blur();
			});
		</script>

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/default.min.css">
		<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/highlight.min.js"></script>
	</head>
	<body>
		<h2 id="regularexpressionregex">Regular Expression (RegEx)</h2>
		<p>While filling online forms, haven't you come across errors like "Please enter valid email address" or "Please enter valid phone number".</p>
		<p>Annoying as they may be, there's a lot of black magic that the computer does before it determines that, the details you've entered are incorrect.</p>
		<p>Can you think out, what is that black magic? If you are familiar with algorithms, then you will say that we can write an algorithm for the same.</p>
		<p>Yes, we can write an algorithm to verify different things, but we have a standard tool designed for similar kinds of purposes.</p>
		<p>It is <strong>Regular Expression</strong>. We call it <strong>RegEx</strong> for short. RegEx makes our work a lot easier. Let's see some basic examples where RegEx becomes handy.</p>
		<p>Suppose, you are in search of an averge price of a particular product on amazon. The following regular expression will find you any price(ex. <code>$12</code>, <code>$75.50</code>) on the webpage: <code>$([0-9]+)\.([0-9]+)</code>. In the Image below, yellowish part shows the matched prices.</p>
		<p><img src="https://lh3.googleusercontent.com/zH7_h0NJ9s5Kf22US-NJDnXL7-QqPXrHc45dc8pCITaIWqJcupyoBuh-ukQiCRCpQQgAIe0UIpBL=s1000" alt="enter image description here" /></p>
		<p>Quite interesting!</p>
		<p>Let's look at another example. You have a long list of documents with different kinds of extensions. You are particularly looking for data files having <strong>.dat</strong> extension. </p>
		<p><code>^.*\.dat$</code> is a regular expression which represents a set of string ending with <strong>.dat</strong>. Regular expression is a standardized way to encode such patterns. </p>
		<p>Below in the image, you can see that all three files having .dat extension are extracted from the list of five files.</p>
		<p><img src="https://lh3.googleusercontent.com/6tFqDs2lLl9h2GiDtPrKZxPGk2hsaykfNwzLQLm1bhW1fOw16uTALMwCKfsKEsnXi5v_hm9NgI23=s1000" alt="enter image description here" /></p>
		<p>Well. What does the name <strong>Regular Expression(RegEx)</strong> represent? Regular Expression represents the sequence of characters that defines a regular search pattern.</p>
		<p>RegEx is a standardized tool to do the following works:</p>
		<ol>
			<li>Find and verify patterns in a string.</li>
			<li>Extract particular data present in the text.</li>
			<li>Replace, split and rearrange particular parts of a string.</li>
		</ol>
		<p>We are going to look at all the three things above.</p>
		<p>Let's begin the journey with RegEx!</p>
		<p><strong>Note:</strong> </p>
		<ol>
			<li><strong>Alpha-numeric character</strong> belongs to anyone of the 0−9,A−Z,a−z ranges.</li>
			<li>String is a sequence of characters and substring is a contiguous part of a string.</li>
		</ol>
		<p><strong>In this article series, we are going to show all examples using live interactive playground, so that you can play with regex.</strong> You can activate playground by just clicking on it.</p>
		<h2 id="simplealphanumericcharactermatching">Simple Alpha-numeric character matching</h2>
		<p>Simple matching of a specific word can be done as following:</p>
		<div class="container">
			<iframe scrolling="no" style="position: absolute; top: -9999em; visibility: hidden;" onload="this.style.position='static'; this.style.visibility='visible';" src="https://regexr.com/4v1lb" class="embed"></iframe>
		</div>
		<p>As you can see it matches "Reg" in the text. Similarly, what will be the match for "Ex" in the same text above?</p>
		<div class="container">
			<iframe scrolling="no" style="position: absolute; top: -9999em; visibility: hidden;" onload="this.style.position='static'; this.style.visibility='visible';" src="https://regexr.com/4vtfd" class="embed"></iframe>
		</div>
		<p>Do you notice anything? It is a <strong>case sensitive</strong>.</p>
		<h2 id="implementation">Implementation</h2>
		<p>Most of the programming languages have libraries for RegEx. They have almost similar kind of syntax. Here, we will see how to implement it in <strong>Javascript</strong>.</p>
		<p>Below is a basic code in Javascript, showing how to implement regex. The patterns are written in <code>/_____/g</code>. Where <code>g</code> is a modifier, which is used to find all matches rather than stopping at the first match.</p>
		<p>The function <strong>exec</strong> returns null, if there is no match and match data otherwise.</p>
<pre><code class="js language-js">var text_to_search_in = "RegEx stands for Regular Expression!";

var pattern = /Reg/g;

// This will print all the data of matches across the whole string
while(result = pattern.exec(text_to_search_in)) {
    console.log(result);
}
</code></pre>
		The output will be:
<pre><code class="js language-js">[
  'Reg',
  index: 0,
  input: 'RegEx stands for Regular Expression!',
  groups: undefined
]
[
  'Reg',
  index: 17,
  input: 'RegEx stands for Regular Expression!',
  groups: undefined
]
</code></pre>
		<p><strong>Note:</strong> <strong>Groups</strong> in the above output is a RegEx concept.</p>

		<script type="text/javascript">
			document.addEventListener('DOMContentLoaded', (event) => {
				document.querySelectorAll('pre code').forEach((block) => {
					hljs.highlightBlock(block);
				});
			});
		</script>
	</body>
</html>
