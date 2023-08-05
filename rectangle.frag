#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
// float rectangle(vec2 st, vec4 lrtb) {
// 	float pct = 1.;
// 	pct *= step(lrtb[0], st.x);
// 	pct *= 1. - step(lrtb[1], st.x);
// 	pct *= 1. - step(lrtb[2], st.y);
// 	pct *= step(lrtb[3], st.y);
// 	return (pct);
// }

float rectangle(vec2 st, vec2 pos, vec2 wh) {
	float pct = 1.;
	pct *= step(pos.x, st.x);
	pct *= step(pos.y, st.y);
	pct *= 1. - step(pos.x + wh[0], st.x);
	pct *= 1. - step(pos.y + wh[1], st.y);
	return (pct);
}
float blurredRectangle(vec2 st, vec2 pos, vec2 wh, float blur) {
	float pct = 1.;
	pct *= step(pos.x - (blur / 2.), st.x);
	pct *= step(pos.y - (blur / 2.), st.y);
	pct *= 1. - step(pos.x + (blur / 2.) + wh[0], st.x);
	pct *= 1. - step(pos.y + (blur / 2.) + wh[1], st.y);
	return (pct);
}

void main() {
	vec2 st = gl_FragCoord.xy / u_resolution.xy;
	vec3 color = vec3(0.0);

    // Each result will return 1.0 (white) or 0.0 (black).
	float left = step(0.1, st.x);   // Similar to ( X greater than 0.1 )
	float bottom = step(0.1, st.y); // Similar to ( Y greater than 0.1 )
	float right = 1. - step(0.9, st.x);
	float top = 1. - step(0.9, st.y);
	float blur = 0.1;
	vec2 bl = smoothstep(vec2(0.1) - (blur / 2.), vec2(0.1) + (blur / 2.), st);
	vec2 tr = 1. - smoothstep(vec2(0.9) - (blur / 2.), vec2(0.9) + (blur / 2.), st);
	float pct = rectangle(st, vec2(0.4, 0.4), vec2(0.2, 0.2));
    // The multiplication of left*bottom will be similar to the logical AND.
	color = vec3(pct);

	gl_FragColor = vec4(color, 1.0);
}