#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
uniform float u_time;

float rectangle(vec2 st, vec2 pos, vec2 wh) {
	float pct = 1.;

	pct *= step(pos.x, st.x);
	pct *= step(pos.y, st.y);
	pct *= 1. - step(pos.x + wh[0], st.x);
	pct *= 1. - step(pos.y + wh[1], st.y);
	return (pct);
}
float BlurredRectangle(vec2 st, vec2 pos, vec2 wh, float blur) {
	float pct = 1.;
	pct *= smoothstep(pos.x - (blur / 2.), pos.x + (blur / 2.), st.x);
	pct *= smoothstep(pos.y - (blur / 2.), pos.y + (blur / 2.), st.y);
	pct *= 1. - smoothstep(pos.x - (blur / 2.) + wh[0], pos.x + (blur / 2.) + wh[0], st.x);
	pct *= 1. - smoothstep(pos.y - (blur / 2.) + wh[1], pos.y + (blur / 2.) + wh[1], st.y);
	return (pct);
}
float parrallelRectangleOutline(vec2 st, vec2 pos, vec2 wh, float stroke) {
	float pct;
	pct = step(pos.x, st.x) - step(pos.x + stroke, st.x);
	pct += step(pos.y, st.y) - step(pos.y + stroke, st.y);
	pct += step(pos.y + wh[1], st.y) - step(pos.y + wh[1] + stroke, st.y);
	pct += step(pos.x + wh[0], st.x) - step(pos.x + wh[0] + stroke, st.x);
	return (pct);
}
float rectangleOutline(vec2 st, vec2 pos, vec2 wh, float stroke) {
	float pct;
	pct = step(pos.x, st.x) - step(pos.x + stroke, st.x);
	pct += step(pos.y, st.y) - step(pos.y + stroke, st.y);
	pct += step(pos.y + wh[1], st.y) - step(pos.y + wh[1] + stroke, st.y);
	pct += step(pos.x + wh[0], st.x) - step(pos.x + wh[0] + stroke, st.x);
	pct *= step(pos.x, st.x);
	pct *= step(pos.y, st.y);
	pct *= 1. - step(pos.x + wh[0] + stroke, st.x);
	pct *= 1. - step(pos.y + wh[1] + stroke, st.y);
	return (pct);
}

void main() {
	vec2 st = gl_FragCoord.xy / u_resolution.xy;
	vec3 color = vec3(0.0);
	float pct;
	float stroke = 0.015 + 0.1 * sin(u_time);
	pct += rectangle(st, vec2(0., (1. / 3.)), vec2(0.15, (1. / 3.) - stroke));
	pct += rectangle(st, vec2(0., (0.)), vec2(0.15, (1. / 3.) - stroke));
	pct += rectangle(st, vec2((0.15) + stroke, (0.9)), vec2(0.2 - stroke, (1. / 3.) - stroke));
	pct += rectangle(st, vec2((0.15) + stroke, (0.6)), vec2(0.2 - stroke, (0.3) - stroke));
	pct += rectangle(st, vec2((0.35) + stroke, (0.6)), vec2(0.3 - stroke, (2. / 3.) - 0.6));
	pct += rectangle(st, vec2((0.15) + stroke, (0.)), vec2(0.25 - stroke, 0.2));
	pct += rectangle(st, vec2((0.15) + stroke, (0.2) + stroke), vec2(0.25 - stroke, 0.2));
	pct += rectangle(st, vec2((0.55) + stroke, (0.2) + stroke), vec2(0.25 - stroke, 0.2));
	pct += rectangle(st, vec2((0.55) + stroke, (0.)), vec2(0.25 - stroke, 0.2));

	pct += rectangle(st, vec2(0.40 + stroke, 0.), vec2(0.15 - stroke, 0.05));
	pct += rectangle(st, vec2(0.40 + stroke, 0.05 + stroke), vec2(0.15 - stroke, 0.55 - 2. * stroke));

	pct += rectangle(st, vec2((0.65) + stroke, (0.9)), vec2(0.15 - stroke, (1. / 3.) - stroke));
	pct += rectangle(st, vec2((0.65) + stroke, (0.6)), vec2(0.15 - stroke, (0.3) - stroke));
	pct += rectangle(st, vec2(0.80 + stroke, (1. / 3.)), vec2(0.30 - stroke, 0.4 - stroke));
	pct += rectangle(st, vec2(0.80 + stroke, (1. / 3.) + 0.4), vec2(0.30 - stroke, 0.4 - stroke));

	float rectangle1 = rectangle(st, vec2(0., (2. / 3.)), vec2(0.15, (1. / 3.)));
	vec3 blue_rectangle = vec3(rectangle1) * vec3(0.1333, 0.0, 1.0);
	float rectangle2 = rectangle(st, vec2(0.35 + stroke, (2. / 3.) + stroke), vec2(0.30 - stroke, (1. / 3.) - stroke));
	vec3 red_rectangle = vec3(rectangle2) * vec3(1.0, 0.0, 0.0);

	float rectangle3 = rectangle(st, vec2(0.80 + stroke, 0.), vec2(0.30 - stroke, (1. / 3.) - stroke));
	vec3 yellow_rectangle = vec3(rectangle3) * vec3(1, 1.0, 0.0);

	color = vec3(pct);
	color += blue_rectangle;
	color += red_rectangle;
	color += yellow_rectangle;
	gl_FragColor = vec4(color, 1.0);
}